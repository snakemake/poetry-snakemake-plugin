from dataclasses import dataclass, field
import json
from typing import Optional
from snakemake_interface_software_deployment_plugins.settings import (
    SoftwareDeploymentProviderSettingsBase,
)
from snakemake_interface_software_deployment_plugins import (
    SoftwareDeploymentProviderBase,
    EnvBase,
    DeployableEnvBase,
    ArchiveableEnvBase,
    EnvSpecBase,
)


# Optional:
# Define settings for your storage plugin (e.g. host url, credentials).
# They will occur in the Snakemake CLI as --sdm-<plugin-name>-<param-name>
# Make sure that all defined fields are 'Optional' and specify a default value
# of None or anything else that makes sense in your case.
# Note that we allow storage plugin settings to be tagged by the user. That means,
# that each of them can be specified multiple times (an implicit nargs=+), and
# the user can add a tag in front of each value (e.g. tagname1:value1 tagname2:value2).
# This way, a storage plugin can be used multiple times within a workflow with different
# settings.
@dataclass
class SoftwareDeploymentProviderSettings(SoftwareDeploymentProviderSettingsBase):
    myparam: Optional[int] = field(
        default=None,
        metadata={
            "help": "Some help text",
            # Optionally request that setting is also available for specification
            # via an environment variable. The variable will be named automatically as
            # SNAKEMAKE_<storage-plugin-name>_<param-name>, all upper case.
            # This mechanism should only be used for passwords, usernames, and other
            # credentials.
            # For other items, we rather recommend to let people use a profile
            # for setting defaults
            # (https://snakemake.readthedocs.io/en/stable/executing/cli.html#profiles).
            "env_var": False,
            # Optionally specify a function that parses the value given by the user.
            # This is useful to create complex types from the user input.
            "parse_func": ...,
            # If a parse_func is specified, you also have to specify an unparse_func
            # that converts the parsed value back to a string.
            "unparse_func": ...,
            # Optionally specify that setting is required when the executor is in use.
            "required": True,
            # Optionally specify multiple args with "nargs": "+"
        },
    )


# Required:
# Implementation of your software deployment provider
# This class can be empty as the one below.
# You can however use it to store global information or check for certain tools
# to be available.
class SoftwareDeploymentProvider(SoftwareDeploymentProviderBase):
    # For compatibility with future changes, you should not overwrite the __init__
    # method. Instead, use __post_init__ to set additional attributes and initialize
    # futher stuff.

    def __post_init__(self):
        # You can e.g. use this method to store global information or check for
        # certain tools to be available.
        # Overwrite the example code below with your own or remove the entire method
        # if not needed.

        # Example code:
        # Here we run conda info to get information about the current conda
        # installation.
        # Important: We use the inherited method self.run() to run the command.
        # This is mandatory since providers can be stacked by the user, such that
        # e.g. this provider is supposed to be used from within a particular environment
        # like a container or an environment module.
        # The self.run() method takes care of that automatically.
        self.conda_info = json.loads(self.run("conda info --json").decode())


class EnvSpec(EnvSpecBase):
    # This class should implement something that describes an existing or to be created
    # environment.
    # It will be automatically added to the environment object when the environment is
    # created or loaded and is available there as attribute self.spec.
    pass


# Required:
# Implementation of an environment object.
# If your environment cannot be archived or deployed, remove the respective methods
# and the respective base classes.
# All errors should be wrapped with snakemake-interface-common.errors.WorkflowError
class Env(EnvBase, DeployableEnvBase, ArchiveableEnvBase):
    # For compatibility with future changes, you should not overwrite the __init__
    # method. Instead, use __post_init__ to set additional attributes and initialize
    # futher stuff.

    def __post_init__(self) -> None:
        # This is optional and can be removed if not needed.
        # Alternatively, you can e.g. prepare anything or set additional attributes.
        pass

    def decorate_shellcmd(self, cmd: str) -> str:
        # Decorate given shell command such that it runs within the environment.
        ...

    def record_hash(self, hash_object) -> None:
        # Update given hash such that it changes whenever the environment
        # could potentially contain a different set of software (in terms of versions or
        # packages). Use self.spec (containing the corresponding EnvSpec object)
        # to determine the hash.
        ...

    # The methods below are optional. Remove them if not needed and adjust the
    # base classes above.

    def deploy(self) -> None:
        # Remove method if not deployable!
        # Deploy the environment to self.deployment_path, using self.spec
        # (the EnvSpec object).

        # When issuing shell commands, the environment should use
        # self.provider.run(cmd: str) -> bytes in order to ensure that it runs within
        # eventual parent environments (e.g. a container or an env module).
        ...

    def record_deployment_hash(self, hash_object) -> None:
        # Remove method if not deployable!
        # Update given hash such that it changes whenever the environment
        # needs to be redeployed, e.g. because its content has changed or the
        # deployment location has changed. The latter is only relevant if the
        # deployment is senstivive to the path (e.g. in case of conda, which patches
        # the RPATH in binaries).
        ...

    def remove(self) -> None:
        # Remove method if not deployable!
        # Remove the deployed environment from self.deployment_path and perform
        # any additional cleanup.
        ...

    def archive(self) -> None:
        # Remove method if not archiveable!
        # Archive the environment to self.provider.archive_path.

        # When issuing shell commands, the environment should use
        # self.provider.run(cmd: str) -> bytes in order to ensure that it runs within
        # eventual parent environments (e.g. a container or an env module).
        ...
