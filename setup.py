import os
from setuptools import find_packages, setup

# determining the directory containing setup.py
setup_path = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(setup_path, "README.md"), encoding="utf-8") as f:
    readme = f.read()

setup(
    # package information
    name="githubcutter",
    packages=find_packages(),
    version="0.3.1-dev",
    description="A tool to setup GitHub repositories using simple YAML templates",
    long_description=readme,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/stracquadaniolab/githubcutter",
    keywords="version-control git automation",
    #  author information
    author="Giovanni Stracquadanio",
    author_email="giovanni.stracquadanio@ed.ac.uk",
    # installation info and requirements
    install_requires=[
        "argh>=0.26",
        "python-dotenv>=0.10",
        "PyYAML>=5.1",
        "PyGithub>=1.43",
        "dotty-dict>=1.1",
    ],
    setup_requires=[],
    # test info and requirements
    test_suite="tests",
    tests_require=[],
    # package deployment info
    include_package_data=False,
    zip_safe=False,
    # all tools have cli interface
    entry_points={"console_scripts": ["githubcutter=githubcutter.cli:main"]},
)
