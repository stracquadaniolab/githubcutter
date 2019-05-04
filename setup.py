import os
from setuptools import find_packages, setup

# determining the directory containing setup.py
setup_path = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(setup_path, 'README.md'), encoding='utf-8') as f:
    readme = f.read()

setup(
    # package information
    name = 'githubcutter',
    packages = find_packages(),
    version = '0.0.1-dev',
    description = 'A cookiecutter-like clone to setup GitHub repos based on templates',
    long_description = readme,
    license = 'MIT',
    url='git@github.com:stracquadaniolab/github-cutter.git',
    keywords='',

    # author information
    author = 'StracquadanioLab',
    author_email = 'giovanni.stracquadanio@ed.ac.uk',

    # installation info and requirements
    install_requires=[],
    setup_requires=[],

    # test info and requirements
    test_suite='tests',
    tests_require=[],

    # package deployment info
    include_package_data=True,
    zip_safe=False,

    # all tools have cli interface
    entry_points={
        'console_scripts': [
            'githubcutter=githubcutter.cli:main',
        ],
    },
)
