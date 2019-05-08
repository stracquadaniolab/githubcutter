# GitHub Cutter : Python package

"""Top-level package for GitHub Cutter."""

__author__ = """StracquadanioLab"""
__email__ = "giovanni.stracquadanio@ed.ac.uk"
__version__ = "0.3.1-dev"

import logging

logging.getLogger(__name__).addHandler(logging.NullHandler())

# defining field constants
# fields costant to dicrease hard coding in the code
REPO_FIELD = "repository"
SETTINGS_PRIVATE_FIELD = "settings.private"
ORGANIZATION_FIELD = "organization"
SETTING_FIELD = "settings"
LABEL_FIELD = "labels"
MILESTONE_FIELD = "milestones"
DUE_ON_FIELD = "due_on"

# env constants
GITHUB_TOKEN_ENV = "GITHUBCUTTER_GITHUB_TOKEN"
