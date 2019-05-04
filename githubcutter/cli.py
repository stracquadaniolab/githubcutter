import logging
import sys

import argh

from dotenv import load_dotenv, find_dotenv

from .commands import create_repository, delete_repository


def main():
    # setting base logging level
    logging.basicConfig(level=logging.ERROR)

    # disabling
    logging.getLogger(__package__).setLevel(logging.DEBUG)

    # loading env
    load_dotenv(find_dotenv(filename=".githubcutter.env"))

    parser = argh.ArghParser()
    parser.add_commands([create_repository, delete_repository])
    parser.dispatch()


if __name__ == "__main__":
    sys.exit(main())
