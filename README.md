# Cookiecutter Machine Learning

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-red.svg)](#python)
[![Commitizen friendly](https://img.shields.io/badge/commitizen-friendly-brightgreen.svg)](https://commitizen-tools.github.io/commitizen/)
[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-brightgreen.svg)](https://conventionalcommits.org)

## Introduction

The objective of this project is to provide a generic machine learning template
for python based projects.

This includes folder structure, testing and documentation tools which should
work well for most small to midsize (in terms of number of features & examples)
projects using a single instance of a machine.

This project template combines simplicity, best practice for folder structure
and good OOP design.

The main idea is that there's much same stuff you do every time when you start
your machine learning project, so wrapping all this shared stuff will help you
to change just the core idea every time you start a new project.

So, here’s a simple template that help you get into your main project faster and
just focus on your core (Model Architecture, Training Flow, etc.).

## Features

### Automatic updates to the projects generated from this cookiecutter

- Powered by `cruft`;
- Keep your project up-to-date with best practices;
- Good base folder structure for many kinds of ML Projects (see below);

### Bells and whistles

- PEP8 is the universally accepted style guide for Python code. PEP 8 code
  compliance is verified using `ruff`;
- Consistent code quality: formatting the code with `ruff`, and `isort`
  for sorting imports
- Testing setup with `pytest` with `coverage` plugin;
- Type checks with [`mypy`](https://mypy.readthedocs.io);
- Security checks with [`safety`](https://github.com/pyupio/safety) and
  [`bandit`](https://github.com/PyCQA/bandit);
- Ready-to-use `.editorconfig`, `.dockerignore`, `.gitignore` and
  `.gitattributes`. You don't have to worry about those things;
- (Optional) [`Hydra`](https://github.com/facebookresearch/hydra) config templates with
  `ray` integration for elegantly configuring complex applications;
- (Optional) [`typer`](https://typer.tiangolo.com) CLI template to get you
  started quickly;
- Simple [`helm`](https://helm.sh/) chart or [`kustomize`](https://kustomize.io/) to deploy to k8s

### Documentation

- Docstring coverage with [`interrogate`](https://github.com/econchick/interrogate);
- Diagrams as code with [`Diagrams`](https://diagrams.mingrammer.com/);
- Documentation with [`MkDocs`](https://www.mkdocs.org)

### Changelog management

- Standard way of committing rules and communicating it using
  [`commitizen`](https://commitizen-tools.github.io/commitizen/)
- Follow [`conventional commits`](https://www.conventionalcommits.org)
- Bump version automatically using [`semantic versioning`](https://semver.org/)
  based on the commits
- Generate a changelog using [`keep a Changelog`](https://keepachangelog.com/)

### Automation

- Ready-to-use [`pre-commit`](https://pre-commit.com) hooks with
  code-formatting and security features;
- Azure pipeline template available;
- Dockerfile linter with [`hadolint`](https://github.com/hadolint/hadolint).

### To start a new project, run

Generate a machine learning project from this template:

```shell
cookiecutter git@github.com:thatmlopsguy/cookiecutter-ml-project.git
```

or for a specific branch, tag, or commit SHA `{SPECIFIC}`, run:

```shell
cookiecutter -c {SPECIFIC} git@github.com:thatmlopsguy/cookiecutter-ml-project.git
```

or using [cruft](https://cruft.github.io/cruft):

```shell
cruft create -c {SPECIFIC} git@github.com:thatmlopsguy/cookiecutter-ml-project.git
```

Follow the prompts; if you are asked to re-download the cookiecutter template,
input `yes`.

Default responses are shown in the squared brackets; to use them, leave your
response blank, and press enter.

After creating the project, you should follow a couple of steps to make sure
everything works automatically.

Head over to the generated README.md file to read about the next steps and a
more in-depth explanation of the generated project's features.

### Optional changes to consider post-project creation

Have an existing project that you created from a template in the past using
Cookiecutter directly?

Consider using the `cruft` package to integrate future `cookiecutter` releases.

```shell
pip3 install cruft[pyproject]
cruft link git@github.com:thatmlopsguy/cookiecutter-ml-project.git
```

### Updating a Project

To update an existing project, that was created using cruft, run `cruft update`
in the root of the project.

If there are any updates, `cruft` will have you review them before applying.

If you accept the changes `cruft` will apply them to your project and update the
`.cruft.json` file for you.

### Input variables

Template generator will ask you to fill some variables.

The input variables, with their default values:

|      **Parameter**       |      **Default value**      | **Description**                                                                                                                 |
| :----------------------: | :-------------------------: | ------------------------------------------------------------------------------------------------------------------------------- |
|      `project_name`      |       `project_name`        | Project Name                                                                                                                    |
|       `repo_name`        |         `repo_name`         | Repository Name                                                                                                                 |
|      `description`       | based on the `project_name` | Brief description of your project.                                                                                              |
|      `organization`      | based on the `project_name` | Name of the organization. We need to generate LICENSE and to specify ownership in `pyproject.toml`.                             |
|        `license`         |            `MIT`            | One of `MIT`, `BSD-3`, `GNU GPL v3.0` and `Apache Software License 2.0`.                                                        |
| `minimal_python_version` |           `3.10`            | Minimal Python version. It is used for builds and formatters `ruff` and `isort`. |
|   `organization_email`   | based on the `organization` | Email for `SECURITY.md` files and to specify the ownership of the project in `pyproject.toml`.                                  |
|        `version`         |           `0.0.0`           | Initial version of the package. Make sure it follows the [`semantic versions`](https://semver.org) specification.                 |
|      `line_length`       |            `120`            | The max length per line (used for codestyle with `ruff` and `isort`). NOTE: This value must be between 50 and 140.             |
| `command_line_interface` |           `none`            | If `typer` is chosen generator will create simple CLI application with [`typer`](https://github.com/tiangolo/typer) library.    |
|          `k8s`           |           `none`            | Choose if [helm](https://helm.sh/) charts or [kustomize](https://kustomize.io/) to deploy to kubernetes


## Contributing

Any contributions are welcome including improving the template and example
projects.

### Submit a Pull Request

Pull requests are welcome, if they're small, atomic, and if they make my own
packaging experience better.

## Development

```shell
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements/requirements-dev.txt
```

## Credits

See [credits](CREDITS.md) for all acknowledgements.

## References

- [Automatically Set Up a New ML Project, Pain Free (voxel51)](https://voxel51.com/blog/automatically-set-up-a-new-ml-project-pain-free/)
- [Cookiecutter-MLOps (dagshub)](https://dagshub.com/DagsHub/Cookiecutter-MLOps/src/example-project)
- [Cookiecutter Data Science](https://drivendata.github.io/cookiecutter-data-science/)