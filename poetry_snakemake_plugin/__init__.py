

from pathlib import Path
from cleo.commands.command import Command
from cleo.helpers import argument
from poetry.plugins.application_plugin import ApplicationPlugin
import subprocess as sp
from jinja2 import Environment, PackageLoader, select_autoescape
import tomli


class ScaffoldSnakemakeExecutorPluginCommand(Command):

    name = "scaffold-snakemake-executor-plugin"
    description = "Scaffolds a snakemake executor plugin by adding recommended dependencies and code snippets."

    def handle(self) -> int:
        # add dependencies
        sp.run(["poetry", "add", "snakemake-interface-executor-plugins"])
        sp.run(["poetry", "add", "--group", "dev", "black", "flake8", "coverage", "pytest", "snakemake"])

        # add skeleton code
        templates = Environment(
            loader=PackageLoader("poetry_snakemake_plugin"),
            autoescape=select_autoescape(),
        )

        with open("pyproject.toml", "rb") as f:
            pyproject = tomli.load(f)

        def render_template(name, dest: Path):
            dest.parent.mkdir(exist_ok=True, parents=True)
            with open(dest, "w") as f:
                f.write(templates.get_template(name).render(pyproject=pyproject))

        module_path = Path(pyproject["tool"]["poetry"]["name"].replace("-", "_"))
        tests_path = Path("tests")
        workflows_path = Path(".github/workflows")

        render_template("init.py.j2", module_path / "__init__.py")
        render_template("tests.py.j2", tests_path / "tests.py")
        render_template("release_please.yml.j2", workflows_path / "release-please.yml")
        render_template("ci.yml.j2", workflows_path / "ci.yml")
        render_template("conventional_prs.yml.j2", workflows_path / "conventional-prs.yml")

        return 0

class ScaffoldSnakemakeExecutorPlugin(ApplicationPlugin):
    def activate(self, application):
        application.command_loader.register_factory(ScaffoldSnakemakeExecutorPluginCommand.name, ScaffoldSnakemakeExecutorPluginCommand)