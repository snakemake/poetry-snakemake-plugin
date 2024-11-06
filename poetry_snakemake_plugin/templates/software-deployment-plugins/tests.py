from typing import Optional, Type
from snakemake_interface_software_deployment_plugins.tests import TestSoftwareDeploymentBase
from snakemake_interface_software_deployment_plugins import SoftwareDeploymentProviderBase
from snakemake_interface_software_deployment_plugins.settings import SoftwareDeploymentProviderSettingsBase


class TestSoftwareDeployment(TestSoftwareDeploymentBase):
    __test__ = True
    deploy = True  # set to True if the provider deploys its envs
    archive = True  # set to True if envs can be archived

    def get_env_spec(self) -> str:
        # Return an env spec query. If deploy == False the env should be present a priori.
        ...

    def get_software_deployment_provider_cls(self) -> Type[SoftwareDeploymentProviderBase]:
        # Return the SoftwareDeploymentProvider class of this plugin
        ...

    def get_software_deployment_provider_settings(self) -> Optional[SoftwareDeploymentProviderSettingsBase]:
        # instantiate StorageProviderSettings of this plugin as appropriate
        ...
