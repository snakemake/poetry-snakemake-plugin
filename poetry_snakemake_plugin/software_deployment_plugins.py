from pathlib import Path
from typing import List

from poetry_snakemake_plugin.common import ScaffoldSnakemakePluginCommandBase


class ScaffoldSnakemakeSoftwareDeploymentPluginCommand(
    ScaffoldSnakemakePluginCommandBase
):
    name = "scaffold-snakemake-software-deployment-plugin"
    description = (
        "Scaffolds a snakemake software deployment plugin by adding recommended "
        "dependencies and code snippets."
    )

    def get_templates(self, module_path: Path, tests_path: Path) -> List[str]:
        return [
            ("software-deployment-plugins/init.py", module_path / "__init__.py"),
            ("software-deployment-plugins/tests.py", tests_path / "test_plugin.py"),
        ]

    def get_plugin_type(self) -> str:
        return "software-deployment"

    def include_snakemake_dev_dependency(self) -> bool:
        return False
