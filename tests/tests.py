import os
from pathlib import Path
import subprocess as sp

import pytest


PLUGIN_TYPES = [
    path.name.removesuffix("-plugins")
    for path in Path("poetry_snakemake_plugin/templates/").glob("*-plugins")
]


@pytest.mark.parameterize("plugin_type", PLUGIN_TYPES)
def test_new_plugin(plugin_type, tmp_path):
    orig_dir = os.getcwd()
    os.chdir(tmp_path)

    plugin_type = f"{plugin_type}-plugin"

    run_subcommand("new", f"snakemake-{plugin_type}-test")
    os.chdir("snakemake-{plugin_type}-test")
    run_subcommand("scaffold-snakemake-{plugin_type}")

    run_subcommand("run", "black", "--check", "--diff", ".")
    run_subcommand("run", "flake8")
    os.chdir(orig_dir)


def run_subcommand(*args):
    cmd = ["poetry"]
    cmd.extend(args)
    sp.run(cmd, check=True)
