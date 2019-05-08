Getting started
===============


Installation
============

Githubcutter can be installed through pip by running:

.. code-block:: bash

    pip install githubcutter

Githubcutter requires a *.githubcutter.env* file to store
your GitHub authentication token; for example, you can put this file in your home directory.

Create a new *.githubcutter.env* file and put the line below:

.. code:: bash

    GITHUBCUTTER_GITHUB_TOKEN=<token>

replacing <token> with the one you obtained from GitHub.

If Githubcutter is properly installed, running without parameters should print:

.. code:: bash

    usage: githubcutter [-h]
                        {create-repository,cr,create,delete-repository,dr,delete,list-repositories,ls,list}
                        ...

Basic usage
===========

Creating a new repository
-------------------------

Githubcutter can create repositories on personal and/or organisation accounts using a YAML template.
This streamlines the process of creating repositories, specificying basic info, creating custom labels,
and adding milestones.

The template file looks like the one below, and the field names match the one expected by the Github API.

.. code:: yaml

    # repository
    repository: "testing"

    # basic repository setting
    settings:
        # is the repo private?
        private: True

        # description
        description: "a new repo"

        # homepage
        homepage: "https://github.com"

        # enable wiki
        has_wiki: True

        # enable issues
        has_issues: True

    # custom labels
    labels:
        -   name: "High-priority"
            color: "000"
            description: "high-priority task for the project"
        -   name: "Low-priority"
            color: "fff"
            description: "low-priority task for the project"

    # custom milestones
    milestones:
        -   title: "ML #1"
            state: "open"
            description: "Important milestone for the project"
            due_on: 01-01-2020
        -   title: "ML #2"
            state: "open"
            description: "Important milestone for the project"
            due_on: 01-01-2020

Githubcutter looks for a `githubcutter.yml` fiel by default.
Therefore, creating a repo can be as easy as running:

.. code:: bash

    githubcutter create

It is also possible to specify an arbitrary template file as follows:

.. code:: bash

    githubcutter create -i myfile.yml

Specify an organization
~~~~~~~~~~~~~~~~~~~~~~~

By default, githubcutter creates a repository in the personal account associated
with the GitHub token.

You can instead specify an organisation in the template file as follows:

.. code:: yaml

    # repository
    repository: "testing"

    organization: "myteam"

    ...

or by using the command line option:

.. code:: bash

    githubcutter create -o myteam

Specifying repository access
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can specify the access level in the template file as follows:

.. code:: yaml

    # repository
    repository: "testing"

    settings:
        private: True

    ...

or by using the command line option:

.. code:: bash

    githubcutter create -p


Important
~~~~~~~~~
Githubcutter prioritizes options specified by command line over those specified
in the template file.

For example, it is possible to reuse the same template for multiple repositories as follows:

.. code:: bash

    githubcutter create -r my_new_app -i template.yml

Listing repositories
--------------------

It is possible to list repositories on a personal account or organization as follows:

.. code:: bash

    githubcutter ls

Deleting repositories
---------------------

It is possible to list repositories on a personal account or organization as follows:

.. code:: bash

    githubcutter delete testing

Adding labels
-------------

It is possible to add labels to an existing repository from a template as follows:

.. code:: bash

    githubcutter add-labels -i template.yaml -r test


