from pathlib import Path
from typing import List

from poetry_snakemake_plugin.common import ScaffoldSnakemakePluginCommandBase


class ScaffoldSnakemakeReportPluginCommand(ScaffoldSnakemakePluginCommandBase):
    name = "scaffold-snakemake-report-plugin"
    description = (
        "Scaffolds a snakemake report plugin by adding recommended "
        "dependencies and code snippets."
    )

    def get_templates(self, module_path: Path, tests_path: Path) -> List[str]:
        return [
            ("report-plugins/init.py", module_path / "__init__.py"),
            ("report-plugins/tests.py", tests_path / "test_plugin.py"),
        ]

    def get_plugin_type(self) -> str:
        return "report"

    def include_snakemake_dev_dependency(self) -> bool:
        return True
