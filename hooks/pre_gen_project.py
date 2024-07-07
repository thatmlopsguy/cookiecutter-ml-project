#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Configuration tasks to be run before the template has been generated."""

import logging
import re
import sys

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("pre_gen_project")

assert (
    "\\" not in "{{ cookiecutter.author_name }}"
), "Don't include backslashes in author name."

PROJECT_SLUG_REGEX = re.compile(r"^[a-z][_a-z0-9]+$")

# Regular expression to check for a valid email address — based on the HTML5 standard
# (https://html.spec.whatwg.org/multipage/input.html#valid-e-mail-address). This is
# more restrictive than the RFC standard; see the comments in this SO answer for
# further information: https://stackoverflow.com/a/201378
REGEX_EMAIL_ADDRESS = re.compile(
    r"^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?"
    r"(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"
)

SEMVER_REGEX = re.compile(
    r"""
        ^
        (?P<major>0|[1-9]\d*)
        \.
        (?P<minor>0|[1-9]\d*)
        \.
        (?P<patch>0|[1-9]\d*)
        (?:-(?P<prerelease>
            (?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)
            (?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*
        ))?
        (?:\+(?P<build>
            [0-9a-zA-Z-]+
            (?:\.[0-9a-zA-Z-]+)*
        ))?
        $
    """,
    re.VERBOSE,
)


def validate_project_name(project_name: str) -> None:
    """Ensure that `project_name` parameter is valid.
    Valid inputs starts with the lowercase letter.
    Followed by any lowercase letters, numbers or underscores.
    Args:
        project_name: current project name
    Raises:
        ValueError: If project_name is not a valid Python module name
    """
    if PROJECT_SLUG_REGEX.fullmatch(project_name) is None:
        link = "https://www.python.org/dev/peps/pep-0008/#package-and-module-names"
        logger.error("Module name should be pep-8 compliant.")
        logger.error(f"  More info: {link}")
        message = f"ERROR: The project name `{project_name}` is not a valid Python module name."
        raise ValueError(message)


def check_valid_email_address_format(email: str) -> None:
    """Check that an email address is of a valid format using regular expressions.
    `Uses a regular expression pattern based on the HTML5 standard for email address
    format <https://html.spec.whatwg.org/multipage/input.html#valid-e-mail-address>`_.
    Args:
        email: An email address to validate.
    Returns:
        None - raises an `AssertionError` if `email` is not a valid email address
        format.
    """
    assert bool(
        re.fullmatch(REGEX_EMAIL_ADDRESS, email)
    ), f"Invalid email address supplied: {email}"


def check_python_version():
    python_major_version = sys.version_info[0]
    python_minor_version = sys.version_info[1]
    # Must remain compatible with Python 2 to provide useful error message.
    warning = f"\nWARNING: You are running cookiecutter using Python {python_major_version}.{python_minor_version}, but a version >= Python 3.7+ is required.\nEither install a more recent version of Python, or use the Docker instructions.\n"

    if (python_major_version == 2) or (
        python_major_version == 3 and python_minor_version < 7
    ):
        logger.warning(warning)
        sys.exit(1)


def validate_semver(version: str) -> None:
    """Ensure version in semver notation.
    Args:
        version: string version. For example 0.1.2 or 1.2.4
    Raises:
        ValueError: If version is not in semver notation
    """
    if SEMVER_REGEX.fullmatch(version) is None:
        message = (
            f"ERROR: The `{version}` is not in semver notation (https://semver.org/)"
        )
        raise ValueError(message)


def validate_line_length(line_length: int) -> None:
    """Validate line_length parameter. Length should be between 50 and 140.
    Args:
        line_length: integer parameter for isort and black formatters
    Raises:
        ValueError: If line_length isn't between 50 and 140
    """
    if not (50 <= line_length <= 140):
        message = f"ERROR: line_length must be between 50 and 140. Got `{line_length}`."
        raise ValueError(message)


def main() -> None:
    try:
        validate_project_name(project_name="{{cookiecutter.project_slug}}")
        check_valid_email_address_format("{{ cookiecutter.author_email }}")
        check_python_version()
        validate_semver(version="{{ cookiecutter.version }}")
        validate_line_length(line_length=int("{{ cookiecutter.line_length }}"))
    except ValueError as ex:
        logger.error(ex)
        sys.exit(1)


if __name__ == "__main__":
    main()

# EOF
