import os
import sys
import logging
from datetime import datetime

from github import Github

import githubcutter
import githubcutter.config
import githubcutter.entity


def create_repository(
    repo_name=None,
    organization=None,
    private=True,
    description=None,
    homepage=None,
    template=None,
):
    # getting the logger for the command
    logger = logging.getLogger(__name__)

    # parameters update
    config = githubcutter.config.Config.load_from_yaml_file(template)

    # updating the config with the
    config[githubcutter.REPO_FIELD] = repo_name
    config[githubcutter.ORGANIZATION_FIELD] = organization
    config[githubcutter.PRIVATE_FIELD] = private
    config[githubcutter.DESCRIPTION_FIELD] = description
    config[githubcutter.HOMEPAGE_FIELD] = homepage

    if config[githubcutter.REPO_FIELD] is None:
        logger.error(
            "No repository specified in either the template file or on the command line."
        )
        sys.exit(-1)

    try:
        # getting the enty responsible for handling the operations
        entity = githubcutter.entity.EntityManager.get_entity(config[githubcutter.ORGANIZATION_FIELD])

        # creating a repository
        repo = entity.create_repo(
            config[githubcutter.REPO_FIELD],
            description=config[githubcutter.DESCRIPTION_FIELD],
            homepage=config[githubcutter.HOMEPAGE_FIELD],
            private=config[githubcutter.PRIVATE_FIELD],
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
