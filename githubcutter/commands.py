import os
import sys
import logging
from datetime import datetime

from github import Github

import githubcutter
import githubcutter.config
import githubcutter.entity


def create_repository(input_filename: "githubcutter template" = "githubcutter.yml",):
    """
        Create a GitHub repository.
    """

    # getting the logger for the command
    logger = logging.getLogger(__name__)

    # parameters update
    config = githubcutter.config.Config.load_from_yaml_file(input_filename)

    try:
        # getting the enty responsible for handling the operations
        entity = githubcutter.entity.EntityManager.get_entity(
            config[githubcutter.ORGANIZATION_FIELD]
        )

        # creating a repository
        repo = entity.create_repo(
            config[githubcutter.REPO_FIELD], **config[githubcutter.SETTING_FIELD]
        )

        # creating labels
        entity.create_labels(repo, config[githubcutter.LABEL_FIELD])

        # creating milestones
        entity.create_milestones(repo, config[githubcutter.MILESTONE_FIELD])

    except KeyError as kex:
        logger.error("Undefined parameter: %s." % kex.args[0])

    except Exception as ex:
        logger.exception(ex)

    finally:
        logger.info("Repository created.")


def delete_repository(repo_name, organization=None):
    """
        Delete a GitHub repository.
    """
    # getting the logger for the command
    logger = logging.getLogger(__name__)

    try:
        # connecting to Github and get the user
        entity = githubcutter.entity.EntityManager.get_entity(organization)

        # deleting the repo
        entity.delete_repo(repo_name)

    except Exception as ex:
        logger.exception(ex)

    finally:
        # logging info
        logger.info("Repository deleted.")

def list_repositories(organization=None):
    """
        List all GitHub repositories for a user or organization.
    """
    # getting the logger for the command
    logger = logging.getLogger(__name__)

    try:
        # connecting to Github and get the user
        entity = githubcutter.entity.EntityManager.get_entity(organization)

        # list of repositories
        repos = sorted(entity.list_repos(), key=lambda x: x.name)
        for r in repos:
            logger.info('{:>50}'.format(r.name))

    except Exception as ex:
        logger.exception(ex)
