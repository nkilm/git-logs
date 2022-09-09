from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))

VERSION = '0.0.1'
DESCRIPTION = 'Bird-eye view of a local git repository'
LONG_DESCRIPTION = 'git-stats displays the statistics of a local git repository by listing all commits based on frequency, author etc'

# Setting up
setup(
    name="git-logs",
    version=VERSION,
    author="Nikhil Mohite",
    author_email="nikhilmohitelhs@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'git','statistics','local repository','git statistics'],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)