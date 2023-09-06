# poetry-snakemake-plugin

[![test coverage: 100%](https://img.shields.io/badge/test%20coverage-100%25-green)](https://github.com/yte-template-engine/yte/blob/main/pyproject.toml#L30)

A plugin for poetry that adds Snakemake-specific functionality.
Currently it supports scaffolding the source code for new Snakemake executor plugins (see https://github.com/snakemake/snakemake-interface-executor-plugins).

This works as follows.
Lets assume that you want to create a snakemake executor plugin with the name `snakemake-executor-plugin-myfancyexecutor`.

```bash

# Install poetry plugin via
poetry self add poetry-snakemake-plugin

# Create a new poetry project via
poetry new snakemake-executor-plugin-myfancyexecutor

cd snakemake-executor-plugin-myfancyexecutor

# Scaffold the project as a snakemake executor plugin
poetry scaffold-snakemake-executor-plugin
```