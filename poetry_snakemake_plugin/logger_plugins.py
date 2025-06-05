from pathlib import Path
from typing import List

from poetry_snakemake_plugin.common import ScaffoldSnakemakePluginCommandBase


class ScaffoldSnakemakeStoragePluginCommand(ScaffoldSnakemakePluginCommandBase):
    name = "scaffold-snakemake-logger-plugin"
    description = (
        "Scaffolds a snakemake logger plugin by adding recommended "
        "dependencies and code snippets."
    )

    def get_templates(self, module_path: Path, tests_path: Path) -> List[str]:
        return [
            ("logger-plugins/init.py", module_path / "__init__.py"),
            ("logger-plugins/tests.py", tests_path / "test_plugin.py"),
        ]

    def get_plugin_type(self) -> str:
        return "logger"

    def include_snakemake_dev_dependency(self) -> bool:
        return False
