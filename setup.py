#!/usr/bin/env python

from setuptools import setup, find_packages

VERSION = "0.0.1"
DESCRIPTION = "Bird-eye view of a local git repository"
LONG_DESCRIPTION = "git-stats displays the statistics of a local git repository by listing all commits based on frequency, author etc"

# Setting up
setup(
    name="git-logs",
    version=VERSION,
    author="Nikhil Mohite",
    author_email="nikhilmohitelhs@gmail.com",
    download_url="https://github.com/nkilm/git-logs",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "git-logs = gitlogs.main:main",
            "gitlogs = gitlogs.main:main"
        ],
    },
    keywords=["python", "git", "statistics", "local repository", "git statistics"],
    classifiers=[
        "Topic :: Utilities",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Version Control :: Git",
        "Programming Language :: Python :: 3",
    ],
)
