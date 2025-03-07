# poetry-snakemake-plugin

[![test coverage: 100%](https://img.shields.io/badge/test%20coverage-100%25-green)](https://github.com/yte-template-engine/yte/blob/main/pyproject.toml#L30)

A plugin for poetry that adds Snakemake-specific functionality.
Currently it supports scaffolding the source code for new Snakemake [executor plugins](https://github.com/snakemake/snakemake-interface-executor-plugins), [storage plugins](https://github.com/snakemake/snakemake-interface-storage-plugins), and [report plugins](https://github.com/snakemake/snakemake-interface-report-plugins).
This works as follows.

## Scaffolding an executor plugin

Lets assume that you want to create a snakemake executor plugin with the name `snakemake-executor-plugin-myfancyexecutor`.

```bash

# Install poetry plugin via
poetry self add poetry-snakemake-plugin@latest

# Create a new poetry project via
poetry new snakemake-executor-plugin-myfancyexecutor

cd snakemake-executor-plugin-myfancyexecutor

# Scaffold the project as a snakemake executor plugin
poetry scaffold-snakemake-executor-plugin

# Next, edit the scaffolded code according to your needs, and publish
# the resulting plugin into a github repository. The scaffold command also 
# creates github actions workflows that will immediately start to check and test
# the plugin.
```

## Scaffolding a storage plugin

Lets assume that you want to create a snakemake storage plugin with the name `snakemake-storage-plugin-myfancystorage`.

```bash

# Install poetry plugin via
poetry self add poetry-snakemake-plugin@latest

# Create a new poetry project via
poetry new snakemake-storage-plugin-myfancystorage

cd snakemake-storage-plugin-myfancystorage

# Scaffold the project as a snakemake executor plugin
poetry scaffold-snakemake-storage-plugin

# Next, edit the scaffolded code according to your needs, and publish
# the resulting plugin into a github repository. The scaffold command also 
# creates github actions workflows that will immediately start to check and test
# the plugin.
```

## Scaffolding a report plugin

Lets assume that you want to create a snakemake report plugin with the name `snakemake-report-plugin-myfancyreport`.

```bash

# Install poetry plugin via
poetry self add poetry-snakemake-plugin@latest

# Create a new poetry project via
poetry new snakemake-report-plugin-myfancyreport

cd snakemake-storage-plugin-myfancyreport

# Scaffold the project as a snakemake executor plugin
poetry scaffold-snakemake-report-plugin

# Next, edit the scaffolded code according to your needs, and publish
# the resulting plugin into a github repository. The scaffold command also 
# creates github actions workflows that will immediately start to check and test
# the plugin.
```

## Scaffold a software deployment plugin

Lets assume that you want to create a snakemake software deployment plugin with the name `snakemake-deployment-plugin-myfancydeployment`.

```bash

# Install poetry plugin via
poetry self add poetry-snakemake-plugin@latest

# Create a new poetry project via
poetry new snakemake-software-deployment-plugin-myfancydeployment

cd snakemake-software-deployment-plugin-myfancydeployment

# Scaffold the project as a snakemake software deployment plugin
poetry scaffold-snakemake-software-deployment-plugin

# Next, edit the scaffolded code according to your needs, and publish
# the resulting plugin into a github repository. The scaffold command also 
# creates github actions workflows that will immediately start to check and test
# the plugin.
```

