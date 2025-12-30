### Hexlet tests and linter status:
[![Actions Status](https://github.com/volkbav/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/volkbav/python-project-52/actions) [![Test task manager](https://github.com/volkbav/python-project-52/actions/workflows/my_tests.yml/badge.svg)](https://github.com/volkbav/python-project-52/actions/workflows/my_tests.yml) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=volkbav_python-project-52&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=volkbav_python-project-52)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=volkbav_python-project-52&metric=coverage)](https://sonarcloud.io/summary/new_code?id=volkbav_python-project-52)
<hr>

# About project
This is a learning project. Completed as part of the python developer course

## demo
To view demo [click here](https://task-manager-5h50.onrender.com)

## Technologies Used
[django](https://www.djangoproject.com/) - Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel.

[uv](https://github.com/astral-sh/uv) - Python package and project manager

[library os](https://docs.python.org/3/library/os.html) - Miscellaneous operating system interfaces

[library dotenv](https://pypi.org/project/python-dotenv/) - Reads key-value pairs from a .env file and can set them as environment variables

[Rollbar](https://rollbar.com/) - Error tracking and deployment quality a part of every project with Terraform provider and REST API.

[Ruff](https://docs.astral.sh/ruff/) - An extremely fast Python linter and code formatter.


# Installation
For work you need make next step
## 1. Install Python
macOs
```
brew install python3
```
linux (ubuntu)
```
sudo apt install python3
```
## 2. Install uv
```
curl -LsSf https://astral.sh/uv/install.sh | sh
```
If you did not have `curl`:
```
wget -qO- https://astral.sh/uv/install.sh | sh
```
macOs
```
brew install uv
```
linux (ubuntu)
```
brew install uv
```
## 3. Clone repository
```
git clone https://github.com/volkbav/python-project-52.git
```
## 4. Install programm
```
make install
```
## 5. app config
For application configuration, you need to:
- modify the .env_example file.  
The description of the variables is inside the file.
- rename .env_example to .env


# Run project
```
make start
```
To view web interface go to adress in brouser
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)