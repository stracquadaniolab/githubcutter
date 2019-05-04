# GitHub Cutter : Python package

"""Top-level package for GitHub Cutter."""

__author__ = """StracquadanioLab"""
__email__ = "giovanni.stracquadanio@ed.ac.uk"
__version__ = "0.0.1-dev"

import logging

logging.getLogger(__name__).addHandler(logging.NullHandler())

# defining field constants
# fields costant to dicrease hard coding in the code
REPO_FIELD = "repository"
DESCRIPTION_FIELD = "description"
HOMEPAGE_FIELD = "homepage"
PRIVATE_FIELD = "private"
WIKI_FIELD = "wiki"
ISSUES_FIELD = "issues"
LABEL_FIELD = "labels"
MILESTONE_FIELD = "milestones"
DUE_ON_FIELD = "due_on"
ORGANIZATION_FIELD = "organization"

# env constants
GITHUB_TOKEN_ENV = "GITHUBCUTTER_GITHUB_TOKEN"
