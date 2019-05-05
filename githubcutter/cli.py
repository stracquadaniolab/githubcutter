import logging
import sys

import argh

from dotenv import load_dotenv, find_dotenv

from .commands import create_repository, delete_repository, list_repositories


def main():
    # setting base logging level
    log_format = "[%(asctime)s %(levelname)s - %(funcName)s]  %(message)s"
    logging.basicConfig(level=logging.ERROR, format=log_format, datefmt="%Y-%m-%d %H:%M:%S")

    # showing log just for githubcutter
    logging.getLogger(__package__).setLevel(logging.DEBUG)

    # loading env
    load_dotenv(find_dotenv(filename=".githubcutter.env"))

    parser = argh.ArghParser()
    parser.add_commands([create_repository, delete_repository, list_repositories])
    parser.dispatch()


if __name__ == "__main__":
    sys.exit(main())
