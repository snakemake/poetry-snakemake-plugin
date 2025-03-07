from dataclasses import dataclass, field
from typing import Iterable, List, Optional
from snakemake_interface_software_deployment_plugins.settings import (
    SoftwareDeploymentProviderSettingsBase,
)
from snakemake_interface_software_deployment_plugins import (
    EnvBase,
    DeployableEnvBase,
    ArchiveableEnvBase,
    EnvSpecBase,
    SoftwareReport,
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


class EnvSpec(EnvSpecBase):
    # This class should implement something that describes an existing or to be created
    # environment.
    # It will be automatically added to the environment object when the environment is
    # created or loaded and is available there as attribute self.spec.
    # Use either __init__ with type annotations or dataclass attributes to define the
    # spec.
    def identity_attributes(self) -> Iterable[str]:
        # Yield the attributes of this subclass that uniquely identify the
        # environment spec. These are used for hashing and equality comparison.
        # For example, the name of the env or the path to the environment definition
        # file or the URI of the container, whatever this plugin uses.
        ...

    def source_path_attributes(self) -> Iterable[str]:
        # Return iterable of attributes of the subclass that represent paths that are
        # supposed to be interpreted as being relative to the defining rule.
        # For example, this would be attributes pointing to conda environment files.
        # Return empty list if no such attributes exist.
        ...


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
        self.check()

    # The decorator ensures that the decorated method is only called once
    # in case multiple environments of the same kind are created.
    @EnvBase.once
    def check(self) -> None:
        # Check e.g. whether the required software is available (e.g. a container
        # runtime or a module command).
        ...

    def decorate_shellcmd(self, cmd: str) -> str:
        # Decorate given shell command such that it runs within the environment.
        ...

    def record_hash(self, hash_object) -> None:
        # Update given hash such that it changes whenever the environment
        # could potentially contain a different set of software (in terms of versions or
        # packages). Use self.spec (containing the corresponding EnvSpec object)
        # to determine the hash.
        hash_object.update(...)

    def report_software(self) -> List[SoftwareReport]:
        # Report the software contained in the environment. This should be a list of
        # snakemake_interface_software_deployment_plugins.SoftwareReport data class.
        # Use SoftwareReport.is_secondary = True if the software is just some
        # less important technical dependency. This allows Snakemake's report to
        # hide those for clarity. In case of containers, it is also valid to
        # return the container URI as a "software".
        # Return an empty list if no software can be reported.
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
