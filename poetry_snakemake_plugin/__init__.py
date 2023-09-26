from poetry.plugins.application_plugin import ApplicationPlugin

from poetry_snakemake_plugin.executor_plugins import (
    ScaffoldSnakemakeExecutorPluginCommand,
)


class ScaffoldSnakemakeExecutorPlugin(ApplicationPlugin):
    def activate(self, application):
        application.command_loader.register_factory(
            ScaffoldSnakemakeExecutorPluginCommand.name,
            ScaffoldSnakemakeExecutorPluginCommand,
        )
