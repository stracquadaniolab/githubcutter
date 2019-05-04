import logging

import yaml


class Config(object):
    def __init__(self, yml_string=None):
        # parsing a YAML string into a Python dict
        if yml_string:
            self.__config = self.__parse_yml(yml_string)
        else:
            self.__config = dict()

    def __setitem__(self, key, value):
        if value is not None:
            self.__config[key] = value

    def __getitem__(self, key):
        if key in self.__config:
            return self.__config[key]
        else:
            return None

    def __parse_yml(self, yml_string):
        try:
            config_dict = yaml.load(yml_string, Loader=yaml.FullLoader)
        except Exception as ex:
            logging.getLogger(__name__).exception(ex)
        else:
            return config_dict

    @staticmethod
    def load_from_yaml_file(fname):
        if fname is None:
            return Config()
        try:
            yml_string = open(fname, "r").read()
            cfg = Config(yml_string)
            return cfg
        except IOError as ex:
            logging.getLogger(__name__).exception(ex)
