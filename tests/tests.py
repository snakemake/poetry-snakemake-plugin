import os
import subprocess as sp


def test_new_snakemake_executor_plugin(tmp_path):
    orig_dir = os.getcwd()
    os.chdir(tmp_path)

    run_subcommand("new", "snakemake-executor-plugin-test")
    os.chdir("snakemake-executor-plugin-test")
    run_subcommand("scaffold-snakemake-executor-plugin")

    run_subcommand("run", "black", "--check", "--diff", ".")
    run_subcommand("run", "flake8")
    os.chdir(orig_dir)


def test_new_snakemake_storage_plugin(tmp_path):
    orig_dir = os.getcwd()
    os.chdir(tmp_path)

    run_subcommand("new", "snakemake-storage-plugin-test")
    os.chdir("snakemake-storage-plugin-test")
    run_subcommand("scaffold-snakemake-storage-plugin")

    run_subcommand("run", "black", "--check", "--diff", ".")
    run_subcommand("run", "flake8")
    os.chdir(orig_dir)


def test_new_snakemake_report_plugin(tmp_path):
    orig_dir = os.getcwd()
    os.chdir(tmp_path)

    run_subcommand("new", "snakemake-report-plugin-test")
    os.chdir("snakemake-report-plugin-test")
    run_subcommand("scaffold-snakemake-report-plugin")

    run_subcommand("run", "black", "--check", "--diff", ".")
    run_subcommand("run", "flake8")
    os.chdir(orig_dir)


def run_subcommand(*args):
    cmd = ["poetry"]
    cmd.extend(args)
    sp.run(cmd, check=True)
