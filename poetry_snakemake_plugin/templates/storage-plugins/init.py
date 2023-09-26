from dataclasses import dataclass, field
from typing import Any, Iterable, List, Generator, Optional, Sequence
from snakemake_interface_storage_plugins.settings import StorageProviderSettingsBase
from snakemake_interface_storage_plugins.storage_provider import StorageProviderBase
from snakemake_interface_storage_plugins.storage_object import (
    AbstractStorageObject,
    retry_decorator,
)
from snakemake_interface_storage_plugins.io import IOCacheStorageInterface, Mtime


# Optional:
# Define settings for your storage plugin (e.g. host url, credentials).
# They will occur in the Snakemake CLI as --storage-<storage-plugin-name>-<param-name>
# Make sure that all defined fields are 'Optional' and specify a default value
# of None or anything else that makes sense in your case.
# Note that we allow storage plugin settings to be tagged by the user. That means,
# that each of them can be specified multiple times (an implicit nargs=+), and
# the user can add a tag in front of each value (e.g. tagname1:value1 tagname2:value2).
# This way, a storage plugin can be used multiple times within a workflow with different
# settings.
@dataclass
class StorageProviderSettings(StorageProviderSettingsBase):
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
            # Optionally specify that setting is required when the executor is in use.
            "required": True,
        },
    )


# Required:
# Implementation of your storage provider
# This class can be empty as the one below.
# You can however use it to store global information or maintain e.g. a connection
# pool.
class StorageProvider(StorageProviderBase):
    def list_objects(self, query: Any) -> Iterable[str]:
        """Return an iterator over all objects in the storage that match the query.

        This is optional and can raise a NotImplementedError() instead.
        """
        ...


# Required:
# Implementation of storage object
class StorageObject(AbstractStorageObject):
    # For compatibility with future changes, you should not overwrite the __init__
    # method. Instead, use __post_init__ to set additional attributes and initialize
    # futher stuff.

    def __post_init__(self):
        # This is optional and can be removed if not needed.
        # Alternatively, you can e.g. prepare a connection to your storage backend here.
        # and set additional attributes.
        pass

    def validate_query(self):
        # validate the query (e.g. URL) stored under self.query
        # This should not perform any lookups, just check that the query is valid
        # from e.g. a syntactical perspective.
        ...

    async def inventory(self, cache: IOCacheStorageInterface):
        """From this file, try to find as much existence and modification date
        information as possible. Only retrieve that information that comes for free
        given the current object.
        """
        # This is optional and can be left as is

        # If this is implemented in a storage object, results have to be stored in
        # the given IOCache object.
        pass

    def get_inventory_parent(self) -> Optional[str]:
        """Return the parent directory of this object."""
        # this is optional and can be left as is
        return None

    def close(self):
        ...

    # Fallible methods should implement some retry logic.
    # The easiest way to do this (but not the only one) is to use the retry_decorator
    # provided by snakemake-interface-storage-plugins.
    @retry_decorator
    def exists(self) -> bool:
        # return True if the object exists
        ...

    @retry_decorator
    def mtime(self) -> Mtime:
        # return the modification time
        ...

    @retry_decorator
    def size(self) -> int:
        # return the size in bytes
        ...

    @retry_decorator
    def retrieve_object(self):
        # Ensure that the object is accessible locally under self.localpath
        ...

    @retry_decorator
    def store_object(self):
        # Ensure that the object is stored at the location specified by self.query.
        # If the storage is read-only, raise NotImplementedError().
        ...

    def list_all_below_ancestor(self) -> Sequence[str]:
        """List all items below the primary ancestor of this object
        (e.g. the bucket name)."""
        # This is optional and can be left as is
        raise NotImplementedError()

    @retry_decorator
    def remove(self):
        # This is optional and can be left as is
        raise NotImplementedError()
