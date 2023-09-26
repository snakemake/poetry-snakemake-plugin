from abc import ABC, abstractmethod
from pathlib import Path
from typing import List
from cleo.commands.command import Command
import subprocess as sp
from jinja2 import Environment, PackageLoader, select_autoescape
import tomli


class ScaffoldSnakemakePluginCommandBase(Command, ABC):
    @abstractmethod
    def get_dependencies(self) -> List[str]:
        ...

    @abstractmethod
    def get_package_name_prefix(self) -> str:
        ...

    @abstractmethod
    def get_templates(self) -> List[str]:
        ...

    def handle(self) -> int:
        # add dependencies
        sp.run(
            ["poetry", "add", "snakemake-interface-common"] + self.get_dependencies()
        )
        sp.run(
            [
                "poetry",
                "add",
                "--group",
                "dev",
                "black",
                "flake8",
                "coverage",
                "pytest",
                "snakemake",
            ]
        )

        # add skeleton code
        templates = Environment(
            loader=PackageLoader("poetry_snakemake_plugin"),
            autoescape=select_autoescape(),
            keep_trailing_newline=True,
        )

        with open("pyproject.toml", "rb") as f:
            pyproject = tomli.load(f)

        package_name = pyproject["tool"]["poetry"]["name"]
        if not package_name.startswith(self.get_package_name_prefix()):
            raise ValueError(
                f"Package name must start with {self.get_package_name_prefix()} "
                f"(found {package_name}))"
            )

        plugin_name = package_name.replace(self.get_package_name_prefix(), "")

        def render_template(name, dest: Path):
            dest.parent.mkdir(exist_ok=True, parents=True)
            with open(dest, "w") as f:
                f.write(
                    templates.get_template(name).render(
                        pyproject=pyproject, plugin_name=plugin_name
                    )
                )

        module_path = Path(pyproject["tool"]["poetry"]["name"].replace("-", "_"))
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
