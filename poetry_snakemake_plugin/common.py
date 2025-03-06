from abc import ABC, abstractmethod
from pathlib import Path
from typing import List
from cleo.commands.command import Command
import subprocess as sp
from jinja2 import Environment, PackageLoader, select_autoescape
import toml


class ScaffoldSnakemakePluginCommandBase(Command, ABC):
    @abstractmethod
    def get_templates(self, module_path: Path, tests_path: Path) -> List[str]: ...

    @abstractmethod
    def get_plugin_type(self) -> str: ...

    def get_dependencies(self) -> List[str]:
        return [f"snakemake-interface-{self.get_plugin_type()}-plugins"]

    @abstractmethod
    def include_snakemake_dev_dependency(self) -> bool: ...

    def get_package_name_prefix(self) -> str:
        return f"snakemake-{self.get_plugin_type()}-plugin-"

    def handle(self) -> int:
        with open("pyproject.toml", "r") as f:
            pyproject = toml.load(f)

        package_name = pyproject["project"]["name"]

        if not package_name.startswith(self.get_package_name_prefix()):
            raise ValueError(
                f"Package name must start with {self.get_package_name_prefix()} "
                f"(found {package_name})"
            )

        plugin_name = package_name.replace(self.get_package_name_prefix(), "")

        pyproject["project"]["repository"] = "https://github.com/your/plugin"
        pyproject["project"]["documentation"] = (
            "https://snakemake.github.io/snakemake-plugin-catalog/plugins/"
            f"{self.get_plugin_type()}/{plugin_name}.html"
        )
        # the python dependency should be in line with the dependencies
        pyproject["project"]["requires-python"] = ">=3.11,<4.0"

        with open("pyproject.toml", "w") as f:
            toml.dump(pyproject, f)

        # add dependencies
        sp.run(
            ["poetry", "add", "snakemake-interface-common"] + self.get_dependencies()
        )
        dev_deps = [
            "poetry",
            "add",
            "--group",
            "dev",
            "ruff",
            "coverage",
            "pytest",
        ]
        if self.include_snakemake_dev_dependency():
            dev_deps.append("snakemake")
        sp.run(dev_deps)

        # add skeleton code
        templates = Environment(
            loader=PackageLoader("poetry_snakemake_plugin"),
            autoescape=select_autoescape(),
            keep_trailing_newline=True,
        )

        def render_template(name, dest: Path):
            dest.parent.mkdir(exist_ok=True, parents=True)
            with open(dest, "w") as f:
                f.write(
                    templates.get_template(name).render(
                        pyproject=pyproject, plugin_name=plugin_name
                    )
                )

        module_path = Path("src") / pyproject["project"]["name"].replace("-", "_")
        tests_path = Path("tests")
        workflows_path = Path(".github/workflows")

        (tests_path / "__init__.py").unlink(missing_ok=True)

        render_template("setup.cfg.j2", Path("setup.cfg"))
        render_template("release_please.yml.j2", workflows_path / "release-please.yml")
        render_template("ci.yml.j2", workflows_path / "ci.yml")
        render_template(
            "conventional_prs.yml.j2", workflows_path / "conventional-prs.yml"
        )

        for template, target in self.get_templates(
            module_path=module_path, tests_path=tests_path
        ):
            render_template(template, target)

        return 0
