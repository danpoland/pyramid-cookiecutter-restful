============================
pyramid-cookiecutter-restful
============================

.. image:: https://travis-ci.org/Pylons/pyramid-cookiecutter-alchemy.png?branch=master
        :target: https://travis-ci.org/danpoland/pyramid-cookiecutter-restful
        :alt: Master Travis CI Status

A Cookiecutter (project template) for creating a Pyramid project using SQLAlchemy for an ORM, URL dispatch for routing, and pyramid-restful-framewor for creating RESTful APIs.

Uses Docker for local development.

Requirements
------------

* Python 2.7 or 3.4+
* `cookiecutter <https://cookiecutter.readthedocs.io/en/latest/installation.html>`_

Usage
-----

1. Generate a Pyramid project, following the prompts from the command.

.. code-block:: bash

    $ cookiecutter https://github.com/danpoland/pyramid-cookiecutter-restful

2. Finish configuring the project by creating a virtual environment and installing your new project. These steps are output as part of the cookiecutter command above and are slightly different for Windows.

.. code-block:: bash

    # Change directory into your newly created project.
    $ cd myproj
    # Create a virtual environment...
    $ python3 -m venv venv
    # ...where we upgrade packaging tools...
    $ env/bin/pip install --upgrade pip setuptools
    # ...and into which we install our project and its testing requirements.
    $ env/bin/pip install -e ".[testing]"
