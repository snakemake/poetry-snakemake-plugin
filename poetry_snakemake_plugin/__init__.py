from poetry.plugins.application_plugin import ApplicationPlugin

from poetry_snakemake_plugin.executor_plugins import (
    ScaffoldSnakemakeExecutorPluginCommand,
)
from poetry_snakemake_plugin.report_plugins import ScaffoldSnakemakeReportPluginCommand
from poetry_snakemake_plugin.storage_plugins import (
    ScaffoldSnakemakeStoragePluginCommand,
)
from poetry_snakemake_plugin.software_deployment_plugins import (
    ScaffoldSnakemakeSoftwareDeploymentPluginCommand,
)


class ScaffoldSnakemakeExecutorPlugin(ApplicationPlugin):
    def activate(self, application):
        application.command_loader.register_factory(
            ScaffoldSnakemakeExecutorPluginCommand.name,
            ScaffoldSnakemakeExecutorPluginCommand,
        )
        application.command_loader.register_factory(
            ScaffoldSnakemakeStoragePluginCommand.name,
            ScaffoldSnakemakeStoragePluginCommand,
        )
        application.command_loader.register_factory(
            ScaffoldSnakemakeReportPluginCommand.name,
            ScaffoldSnakemakeReportPluginCommand,
        )
        application.command_loader.register_factory(
            ScaffoldSnakemakeSoftwareDeploymentPluginCommand.name,
            ScaffoldSnakemakeSoftwareDeploymentPluginCommand,
        )
