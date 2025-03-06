from pathlib import Path
from typing import List

from poetry_snakemake_plugin.common import ScaffoldSnakemakePluginCommandBase


class ScaffoldSnakemakeExecutorPluginCommand(ScaffoldSnakemakePluginCommandBase):
    name = "scaffold-snakemake-executor-plugin"
    description = (
        "Scaffolds a snakemake executor plugin by adding recommended "
        "dependencies and code snippets."
    )

    def get_templates(self, module_path: Path, tests_path: Path) -> List[str]:
        return [
            ("executor-plugins/init.py", module_path / "__init__.py"),
            ("executor-plugins/tests.py.j2", tests_path / "test_plugin.py"),
        ]

    def get_plugin_type(self) -> str:
        return "executor"

    def include_snakemake_dev_dependency(self) -> bool:
        return True
