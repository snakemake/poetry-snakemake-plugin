import os
import subprocess as sp


def test_new_snakemake_executor_plugin(tmp_path):
    orig_dir = os.getcwd()
    os.chdir(tmp_path)

    run_subcommand("new", "test-plugin")
    os.chdir("test-plugin")
    run_subcommand("scaffold-snakemake-executor-plugin")

    run_subcommand("run", "black", "--check", "--diff", ".")
    run_subcommand("run", "flake8")
    os.chdir(orig_dir)


def run_subcommand(*args):
    cmd = ["poetry"]
    cmd.extend(args)
    sp.run(cmd, check=True)
