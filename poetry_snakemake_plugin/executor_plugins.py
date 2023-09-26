from pathlib import Path
from typing import List

from poetry_snakemake_plugin.common import ScaffoldSnakemakePluginCommandBase


class ScaffoldSnakemakeExecutorPluginCommand(ScaffoldSnakemakePluginCommandBase):
    name = "scaffold-snakemake-executor-plugin"
    description = (
        "Scaffolds a snakemake executor plugin by adding recommended "
        "dependencies and code snippets."
    )

    def get_dependencies(self) -> List[str]:
        return ["snakemake-interface-executor-plugins"]

    def get_package_name_prefix(self) -> str:
        return "snakemake-executor-plugin-"

    def get_templates(self, module_path: Path, tests_path: Path) -> List[str]:
        return [
            ("executor-plugins/init.py", module_path / "__init__.py"),
            ("executor-plugins/tests.py.j2", tests_path / "tests.py"),
        ]
