from pathlib import Path
from typing import List, Tuple

from setuptools import setup, find_packages


NAME=""
DESCRIPTION=""
AUTHOR=""
AUTHOR_EMAIL=""
LICENSE=""
REQUIRES_PYTHON = ">=3.9.0"
ROOT = Path(__file__).parent

try:
    with open(ROOT / "README.md", encoding="utf-8") as f:
        long_description = "\n" + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

def get_version():
    pass

def get_requirements(filename: str = "requirements.txt") -> Tuple[List[str], List[str]]:
    requirements = []
    extra_indices = []
    with open(ROOT / "requirements" / filename) as f:
        for line in f.readlines():
            line = line.rstrip("\r\n")
            if line.startswith("--extra-index-url "):
                extra_indices.append(line[18:])
                continue
            requirements.append(line)
    return requirements, extra_indices

requirements, extra_indices = get_requirements()
dev_requirements, _ = get_requirements("requirements-dev.txt")
docs_requirements, _ = get_requirements("requirements-docs.txt")
tests_requirements, _ = get_requirements("requirements-test.txt")


setup(
    name=NAME,
    version=get_version(),
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='',
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license=LICENSE,
    packages=find_packages(),
    zip_safe=False,
    python_requires=REQUIRES_PYTHON,
    install_requires=requirements,
    tests_require=tests_requirements,
    extras_require={
        "dev": dev_requirements,
        "docs": docs_requirements,
    },
    classifiers=[
        'Intended Audience :: Science/Research',
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ]
)
