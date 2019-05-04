import os

import logging
from datetime import datetime

from github import Github

import githubcutter


class Entity(object):
    def __init__(self, ent):
        self.__entity = ent
        self.__logger = logging.getLogger(__name__)

    def create_repo(self, repo_name, description, homepage, private):
        self.__logger.info("Creating repository: %s." % repo_name)
        return self.__entity.create_repo(repo_name, description, homepage, private)

    def delete_repo(self, repo_name):
        self.__logger.info("Deleting repository: %s." % repo_name)
        repo = self.__entity.get_repo(repo_name)
        repo.delete()

    def create_labels(self, repo, labels, purge=True):
        # purge old labels first
        if purge:
            default_labels = repo.get_labels()
            for l in default_labels:
                l.delete()

        if labels is not None:
            self.__logger.info("Creating labels.")
            # create the new labels
            for cl in labels:
                repo.create_label(**cl)

    def create_milestones(self, repo, milestones):
        if milestones is not None:
            self.__logger.info("Creating milestones.")
            # creating milestones
            for ml in milestones:
                # converting dates to datetime if needed
                if githubcutter.DUE_ON_FIELD in ml:
                    ml[githubcutter.DUE_ON_FIELD] = datetime.strptime(
                        ml[githubcutter.DUE_ON_FIELD], "%d-%m-%Y"
                    )
                repo.create_milestone(**ml)


class EntityManager(object):
    @staticmethod
    def get_entity(organization=None):
        # connecting to Github and get the user
        try:
            gh = Github(os.getenv(githubcutter.GITHUB_TOKEN_ENV))
            if organization:
                entity = gh.get_organization(organization)
            else:
                entity = gh.get_user()
        except KeyError as kex:
            logging.getLogger(__name__).exception(kex)
        finally:
            return Entity(entity)

