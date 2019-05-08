import os
import sys
import logging
from datetime import datetime

from argh import arg, aliases
from argh import wrap_errors, CommandError
from github import Github
from github.GithubException import GithubException

import githubcutter
import githubcutter.config
import githubcutter.entity


@arg(
    "--repository",
    "-r",
    help="name of repository.",
    required=False,
    dest=githubcutter.REPO_FIELD,
)
@arg(
    "--private",
    "-p",
    help="create a public repository.",
    required=False,
    action="store_true",
    dest=githubcutter.SETTINGS_PRIVATE_FIELD,
)
@arg(
    "--organization",
    "-o",
    help="create a repository inside an organization.",
    required=False,
    dest=githubcutter.ORGANIZATION_FIELD,
)
@aliases("cr", "create")
@wrap_errors([GithubException])
def create_repository(
    input_filename: "githubcutter template" = "githubcutter.yml", **kwargs
):
    """
        Create a GitHub repository.
    """
    # parameters update
    config = githubcutter.config.Config.load_from_yaml_file(input_filename)
    # checking for parameters ovverriden by CLI
    config.update(kwargs)

    # getting the enty responsible for handling the operations
    entity = githubcutter.entity.EntityManager.get_entity(
        config[githubcutter.ORGANIZATION_FIELD]
    )

    # creating a repository
    repo = entity.create_repo(
        config[githubcutter.REPO_FIELD], config[githubcutter.SETTING_FIELD]
    )

    # creating labels
    entity.create_labels(repo, config[githubcutter.LABEL_FIELD])

    # creating milestones
    entity.create_milestones(repo, config[githubcutter.MILESTONE_FIELD])


@aliases("dr", "delete")
@wrap_errors([GithubException])
def delete_repository(repo_name, organization=None):
    """
        Delete a GitHub repository.
    """
    # getting the logger for the command
    logger = logging.getLogger(__name__)

    # connecting to Github and get the user
    entity = githubcutter.entity.EntityManager.get_entity(organization)

    # deleting the repo
    entity.delete_repo(repo_name)


@aliases("ls", "list")
@wrap_errors([GithubException])
def list_repositories(organization=None):
    """
        Get the list of GitHub repositories.
    """
    # getting the logger for the command
    logger = logging.getLogger(__name__)

    # connecting to Github and get the user
    entity = githubcutter.entity.EntityManager.get_entity(organization)

    # list of repositories
    repos = sorted(entity.list_repos(), key=lambda x: x.name)
    for r in repos:
        logger.info("{:>50}".format(r.name))


@arg(
    "--repository",
    "-r",
    help="name of repository.",
    required=False,
    dest=githubcutter.REPO_FIELD,
)
@wrap_errors([GithubException])
def add_labels(
    input_filename: "githubcutter template" = "githubcutter.yml",
    purge: "remove existing labels. " = False,
    **kwargs
):
    "Add labels to a repository from a template."
    # parameters update
    config = githubcutter.config.Config.load_from_yaml_file(input_filename)
    # checking for parameters overide by CLI
    config.update(kwargs)

    # getting the entry responsible for handling the operations
    entity = githubcutter.entity.EntityManager.get_entity(
        config[githubcutter.ORGANIZATION_FIELD]
    )

    # getting the repo
    repo = entity.get_repo(config[githubcutter.REPO_FIELD])

    # creating labels
    entity.create_labels(repo, config[githubcutter.LABEL_FIELD], purge=purge)
