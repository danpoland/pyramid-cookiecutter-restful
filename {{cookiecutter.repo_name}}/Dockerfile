FROM python:3.6
MAINTAINER {{ cookiecutter.maintainer_name }} <{{ cookiecutter.maintainer_email }}>

COPY ./setup.py /srv/{{ cookiecutter.project_name }}/{{ cookiecutter.repo_name }}/

RUN pip install -e /srv/{{ cookiecutter.project_name }}/{{ cookiecutter.repo_name }}/

COPY ./{{ cookiecutter.repo_name }} /srv/{{ cookiecutter.project_name }}/{{ cookiecutter.repo_name }}/

WORKDIR  /srv/{{ cookiecutter.project_name }}/{{ cookiecutter.repo_name }}/

EXPOSE 8000