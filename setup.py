#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name="rae",
    version="0.0.1",
    description="Demonstrate RAE paper",
    author="",
    author_email="",
    url="https://github.com/olliethomas/rae",
    install_requires=[
        "torch",
        "torchvision",
        "typing-extensions >= 3.7.2",
        "pandas",
        "seaborn",
    ],
    extras_require={
        "dev": ["black", "mypy", "data-science-types", "pre-commit", "pytest"]
    },
    packages=find_packages(),
)
