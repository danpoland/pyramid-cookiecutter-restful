from setuptools import setup, find_packages


requires = [
    'alembic',
    'pyramid',
    'pyramid-tm',
    'SQLAlchemy',
    'transaction',
    'zope.sqlalchemy',
    'marshmallow',
    'pyramid-restful-framework'
]

tests_require = [
    'WebTest >= 1.3.1',  # py3 compat
    'pytest',
    'pytest-cov',
]

setup(
    name='{{ cookiecutter.repo_name }}',
    version='0.0',
    description='{{ cookiecutter.project_name }}',
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Pyramid',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],
    author='',
    author_email='',
    url='',
    keywords='web pyramid pylons',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    extras_require={
        'testing': tests_require,
    },
    install_requires=requires
)
