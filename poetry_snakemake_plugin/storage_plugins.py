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
