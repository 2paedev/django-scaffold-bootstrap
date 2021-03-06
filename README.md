# django-scaffold-bootstrap

* [Getting started](#Getting-started)
    * [Prerequisites](#Prerequisites)
    * [Installing](#Installing)
* [Testing](#Testing)
	* [Running the unit tests](#running-the-unit-tests)
	* [Coverage](#Coverage)
    * [pre-push hook](#pre-push-hook)
* [Common tools/libraries](#Common-tools/Libraries)
    * [Pipenv](#Pipenv)
    * [django-cors-headers](#django-cors-headers)
    * [django-ratelimit](#django-ratelimit)
* [Dev tools](#Dev-tools)
    * [Pylint](#Pylint)
        * [VScode](#VSCode)
        * [Commands](#Commands)
        * [pre-commit pylint hook](#Pre-commit-Pylint-hook)
    * [Jupyter](#Jupyter)
        * [Notebooks](#Notebooks)
        * [iPython](#iPython)
* [Environments](#Environments)
* [Databases](#Databases)
    * [Environment variables](#Environment-variables)
* [Deployment](#Deployment)
* [Miscellaneous](#Miscellaneous)
	* [Built with](#Built-with)
	* [Contributing](#Contributing)
    * [Versioning](#Versioning)
    * [Authors](#Authors)
    * [License](#License)

*A complete scaffolding bootstrap to Django project. It include linter, notebooks, testing, environments and much more.*

*Fork and play!*

## GETTING STARTED

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. Set a multiple dev tools and see deployment for notes on how to deploy the project on a live system.

All tools are tested and configured with Ubuntu 18.10 and VSCode as IDE.


### Prerequisites

Previously, you need to have installed in your PC:
* Python3.6 (3.6.7-Last official version in Ubuntu 18.10)
* Pip3
* Pipenv
```
$> python3 --version
$> pip3 --version
$> pipenv --version
```

### Installing

Fork the project, clone and go to the project root folder:
```
$> cd django-scaffold-bootstrap
```

Create the environment:
```
$> pipenv shell
```

Install all packages and their dependencies:
```
$> pipenv install
```

Make migrations and create superuser:
```
$> python manage.py makemigrations
$> python manage.py migrate
$> python manage.py createsuperuser
```

Run the server:
```
$> python manage.py runserver
```

## TESTING

Explain what these tests test and why

### Running the unit tests

To execute manually all unit test in the project, run:

```
$> python manage.py tests
```

### Coverage

Explain what these tests test and why

```
Give an example
```

### pre-push hook
To add pre-push hook, run this command:
```
$> cd <path_to_project>
$> cp tools/pre-push .git/hooks
```

## COMMON TOOLS/LIBRARIES

### Pipenv 
(*[Official documentation](https://pipenv.readthedocs.io/en/latest/)*)

To install Pipenv in your SO:
```
$> pip3 install --user pipenv
$> pipenv --version
```
You must see something like this: ***pipenv, version 2018.11.26***

The environment variables are all of them declared on *.env* file at the root folder of the project, next to the Pipfile.

**WARNING: You must uncomment the line in the .gitignore file, especially in production. It contains sensitive data.**

Also, if you wish generate a **requirements.txt** file, write the next command:
```
$> pipenv lock -r > requirement.txt
```

### django-cors-headers 
(*[Official documentation](https://pypi.org/project/django-cors-headers/)*)

Each environment has its own configuration about CORS. You can see the settings numbers. It can be setted in the respective settings files.

### django-ratelimit 
(*[Official documentation](https://django-ratelimit.readthedocs.io/en/stable/)*)

TODO: Info sobre esto

## DEV TOOLS

### Pylint 
(*[Official documentation](https://www.pylint.org/)*)

Pylint and pylint-django is installed as dev package. You must activate it in your favourite IDE.

#### ***VSCode***
In VSCode, install [python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) and modify your user/workspace settings:
```
"python.linting.pylintArgs": [
    "--disable=C0111",
	"--load-plugins",
	"pylint_django"
],
"python.pythonPath": "<python3_path>/python3",
"python.linting.pylintPath": "<installation_path>/bin/pylint"
```

To know the installation path, write this command in terminal:
```
$> which pylint
$> which python3
```

In the project root folder there are a **.pylintrc** file with all pylint config.\

#### ***Commands***
Lint a module:
```
$> pylint <module_name>
$> pylint --load-plugins pylint_django --disable=C0111 <module_name>
```

#### ***pre-commit Pylint hook*** 
(*[Official documentation](https://git-pylint-commit-hook.readthedocs.io/en/latest/)*)

También, instalamos como dev package "git-pylint-commit-hook ". Para configurarlo hay que hacer lo siguiente:
```
$> which pylint
$> git-pylint-commit-hook --pylint <installation_pylint_path>/bin/pylint
$> git-pylint-commit-hook --pylintrc <project_root_folder>/.pylintrc
```

To add pre-commit hook, run this command:
```
$> cd <path_to_project>
$> cp tools/pre-push .git/push
```
 
Con esto ya tendríamos una verificación de linter antes de poder hacer commit.\
More info about the plugin [here](https://git-pylint-commit-hook.readthedocs.io/en/latest/index.html).

### Jupyter

#### Notebooks
(*[Official documentation](https://jupyter-notebook.readthedocs.io/en/stable/)*)

To create a notebook:
```
$> python manage.py shell_plus --notebook
```

#### iPython
(*[Official documentation](https://ipython.readthedocs.io/en/stable/)*)

To use this shell:
```
$> python manage.py shell_plus
```

## ENVIRONMENTS
The project is configured to have 4 environments. The settings are specific for each environment:

* local
* dev
* pre
* pro

## DATABASES
We can choose between an SQLite, PostgreSQL or without a database. If nothing is specified in the .env file, an SQLite is loaded by default.

### Environment variables
We have the following variables in the .env file:
```
DATABASE_ENGINE=''
DATABASE_NAME=''
DATABASE_USER=''
DATABASE_PASSWORD=''
DATABASE_HOST=''
DATABASE_PORT=''
```

#### SQLite
For a development environment or just to test, I advise the installation of a SQLite database.

Just set the variable *DATABASE_ENGINE="sqlite"* and **db.sqlite3** file will be created.

#### PostgreSQL
To use this type of database:

```
DATABASE_ENGINE='postgre'
DATABASE_NAME='my_database'
DATABASE_USER='2pae'
DATABASE_PASSWORD='2pae1234'
DATABASE_HOST='localhost'
DATABASE_PORT=''
```

#### No DB
If you do not need any database, you can configure it like this:
```
DATABASE_ENGINE="no_db"
```


## DEPLOYMENT

Add additional notes about how to deploy this on a live system


## MISCELLANEOUS

### Built With

* [Python](https://www.python.org/) - Interpreted, high-level, general-purpose programming language.
* [Django](https://www.djangoproject.com/) - The web framework used.

### Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

### Versioning

TODO: REPASAR
We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

### Authors

* **2paedev** - *All work* - [Github](https://github.com/2paedev)

See also the list of [contributors](https://github.com/2paedev/django-scaffold-bootstrap/contributors) who participated in this project.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
