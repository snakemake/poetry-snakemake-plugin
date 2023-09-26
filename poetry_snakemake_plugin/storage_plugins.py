from abc import ABC, abstractmethod
from pathlib import Path
from typing import List
from cleo.commands.command import Command
from poetry.plugins.application_plugin import ApplicationPlugin
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

        plugin_name = pyproject["tool"]["poetry"]["name"].replace(
            self.get_package_name_prefix(), ""
        )

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


from pathlib import Path
from typing import List

from poetry_snakemake_plugin.common import ScaffoldSnakemakePluginCommandBase


class ScaffoldSnakemakeStoragePluginCommand(ScaffoldSnakemakePluginCommandBase):
    name = "scaffold-snakemake-storage-plugin"
    description = (
        "Scaffolds a snakemake storage plugin by adding recommended "
        "dependencies and code snippets."
    )

    def get_dependencies(self) -> List[str]:
        return ["snakemake-interface-storage-plugins"]

    def get_package_name_prefix(self) -> str:
        return "snakemake-storage-plugin-"

    def get_templates(self, module_path: Path, tests_path: Path) -> List[str]:
        return [
            ("storage-plugins/init.py", module_path / "__init__.py"),
            ("storage-plugins/tests.py", tests_path / "tests.py"),
        ]
