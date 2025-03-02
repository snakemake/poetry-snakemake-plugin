from typing import Optional, Type
from snakemake_interface_software_deployment_plugins.tests import (
    TestSoftwareDeploymentBase,
)
from snakemake_interface_software_deployment_plugins import (
    SoftwareDeploymentProviderBase,
    EnvSpecBase,
)
from snakemake_interface_software_deployment_plugins.settings import (
    SoftwareDeploymentProviderSettingsBase,
)


class TestSoftwareDeployment(TestSoftwareDeploymentBase):
    __test__ = True  # activate automatic testing

    def get_software_deployment_provider_class(
        self,
    ) -> Type[SoftwareDeploymentProviderBase]:
        # Return the SoftwareDeploymentProvider class of this plugin
        ...

    def get_software_deployment_provider_settings(
        self,
    ) -> Optional[SoftwareDeploymentProviderSettingsBase]:
        # instantiate StorageProviderSettings of this plugin as appropriate or return
        # None if no settings are required
        ...

    def get_env_spec(self) -> EnvSpecBase:
        # Return an env spec query.
        # If the software deployment provider does not support deployable environments,
        # this method should return an existing environment spec that can be used for
        # testing
        ...

    def get_test_cmd(self) -> str:
        # Return a command that should be executable without error in the environment
        ...
