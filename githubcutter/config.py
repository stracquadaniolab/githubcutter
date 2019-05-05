import logging

import yaml


class Config(object):
    def __init__(self, yml_string=None):
        # parsing a YAML string into a Python dict
        self.__config = self.__parse_yml(yml_string)

    def __setitem__(self, key, value):
        self.__config[key] = value

    def __getitem__(self, key):
        val = None
        try:
            val =  self.__config[key]
        except KeyError as kex:
            logging.getLogger(__name__).error("Missing config parameter: %s." % kex.args[0])
        finally:
            return val

    def __parse_yml(self, yml_string):
        try:
            config_dict = yaml.load(yml_string, Loader=yaml.FullLoader)
        except Exception as ex:
            logging.getLogger(__name__).exception(ex)
        else:
            return config_dict

    @staticmethod
    def load_from_yaml_file(fname):
        try:
            yml_string = open(fname, "r").read()
            cfg = Config(yml_string)
            return cfg
        except IOError as ex:
            logging.getLogger(__name__).exception(ex)
