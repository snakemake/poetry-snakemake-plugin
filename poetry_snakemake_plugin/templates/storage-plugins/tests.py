from typing import Optional, Type
from snakemake_interface_storage_plugins.tests import TestStorageBase
from snakemake_interface_storage_plugins.storage_provider import StorageProviderBase
from snakemake_interface_storage_plugins.settings import StorageProviderSettingsBase


class TestStorage(TestStorageBase):
    __test__ = True
    retrieve_only = False  # set to True if the storage is read-only
    store_only = False  # set to True if the storage is write-only
    delete = True  # set to False if the storage does not support deletion

    def get_query(self, tmp_path) -> str:
        # Return a query. If retrieve_only is True, this should be a query that
        # is present in the storage, as it will not be created.
        ...

    def get_query_not_existing(self, tmp_path) -> str:
        ...

    def get_storage_provider_cls(self) -> Type[StorageProviderBase]:
        # Return the StorageProvider class of this plugin
        ...

    def get_storage_provider_settings(self) -> Optional[StorageProviderSettingsBase]:
        # instantiate StorageProviderSettings of this plugin as appropriate
        ...
