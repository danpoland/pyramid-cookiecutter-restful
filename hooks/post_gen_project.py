import os
import subprocess
import sys

from textwrap import dedent

WIN = sys.platform.startswith('win')

venv = 'env'
if WIN:
    venv_cmd = 'py -3 -m venv'
    venv_bin = os.path.join(venv, 'Scripts')
else:
    venv_cmd = 'python3 -m venv'
    venv_bin = os.path.join(venv, 'bin')

vars = dict(
    separator='=' * 79,
    venv=venv,
    venv_cmd=venv_cmd,
    pip_cmd=os.path.join(venv_bin, 'pip'),
    pytest_cmd=os.path.join(venv_bin, 'pytest'),
)
msg = dedent(
    """
    Change directory into your newly created project.
        cd {{ cookiecutter.repo_name }}

    Create a Python virtual environment.
        %(venv_cmd)s %(venv)s

    Upgrade packaging tools.
        %(pip_cmd)s install --upgrade pip setuptools

    Install the project in editable mode with its testing requirements.
        %(pip_cmd)s install -e ".[testing]"

    Run your project's tests.
        %(pytest_cmd)s

    Run your project.
        Create a docker compose file and set the required environment vars.
    """ % vars)
print(msg)
