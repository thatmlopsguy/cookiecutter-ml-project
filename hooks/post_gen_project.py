#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Configuration tasks to be run after the template has been generated."""


import contextlib
import logging
import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("post_gen_project")

TERMINATOR = "\x1b[0m"
WARNING = "\x1b[1;33m [WARNING]: "
INFO = "\x1b[1;33m [INFO]: "
HINT = "\x1b[3;33m"
SUCCESS = "\x1b[1;32m [SUCCESS]: "


def remove_temp_folders(temp_folders) -> None:
    for folder in temp_folders:
        logger.info("Remove temporary folder: %s", folder)
        shutil.rmtree(folder)


def remove_file(file_path) -> None:
    if os.path.exists(file_path):
        os.remove(os.path.join(PROJECT_DIRECTORY, file_path))


def remove_files(files):
    for file in files:
        with contextlib.suppress(IOError):
            os.remove(file)


def remove_folder(folder_path) -> None:
    if os.path.exists(folder_path):
        shutil.rmtree(os.path.join(PROJECT_DIRECTORY, folder_path))


def setup_git_repo(version: str = "0.0.0") -> None:
    logger.info("Setting up git branches ...")
    os.system("git init && git checkout -b cookiecutter && git add --all")
    os.system('git commit --allow-empty -n -m "Initial commit by cookiecutter."')
    os.system(f'git tag -a v{version} -m "Release tag for version {version}"')

def main() -> None:
    project_slug = "{{ cookiecutter.project_slug }}"
    version = "{{ cookiecutter.version }}"
    if "{{ cookiecutter.license }}" == "Proprietary":
        remove_file("LICENSE")
    if "{{ cookiecutter.experiment_tracking }}" in ["none"]:
        remove_file(".mlflow")

    logger.info(
        f"{SUCCESS}Project initialized successfully! You can now jump to {project_slug} folder{TERMINATOR}"
    )
    logger.info(
        f"{INFO}{project_slug}/README.md contains instructions on how to proceed.{TERMINATOR}"
    )
    setup_git_repo(version=version)


if __name__ == "__main__":
    main()

# EOF
