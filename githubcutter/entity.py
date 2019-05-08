import os
import logging
from datetime import datetime

from github import Github
import githubcutter


class Entity(object):
    def __init__(self, ent):
        self.__entity = ent
        self.__logger = logging.getLogger(__name__)

    def create_repo(self, repo_name, params=None):
        self.__logger.info("Creating repository: %s." % repo_name)
        if params:
            return self.__entity.create_repo(repo_name, **params)
        else:
            return self.__entity.create_repo(repo_name)
        self.__logger.info("Repository created.")

    def get_repo(self, repo_name):
        self.__logger.info("Getting repository: %s." % repo_name)
        return self.__entity.get_repo(repo_name)

    def delete_repo(self, repo_name):
        self.__logger.info("Deleting repository: %s." % repo_name)
        repo = self.__entity.get_repo(repo_name)
        repo.delete()
        self.__logger.info("Repository deleted.")

    def list_repos(self):
        return self.__entity.get_repos()

    def create_labels(self, repo, labels, purge=True):
        # purge old labels first
        if purge:
            default_labels = repo.get_labels()
            for l in default_labels:
                l.delete()

        if labels:
            self.__logger.info("Creating labels.")
            # create the new labels
            for cl in labels:
                repo.create_label(**cl)
            self.__logger.info("Labels created.")

    def create_milestones(self, repo, milestones):
        if milestones:
            self.__logger.info("Creating milestones.")
            # creating milestones
            for ml in milestones:
                # converting dates to datetime if needed
                if githubcutter.DUE_ON_FIELD in ml:
                    ml[githubcutter.DUE_ON_FIELD] = datetime.strptime(
                        ml[githubcutter.DUE_ON_FIELD], "%d-%m-%Y"
                    )
                repo.create_milestone(**ml)
            self.__logger.info("Milestones created.")


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

