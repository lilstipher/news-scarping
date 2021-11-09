# news-api
News api 


## Description
A simple news api built with fastapi (python 3.9)

## How to setup everything

- First setup a virtual env 
Ex :
```bash
python -m venv .venv
source .venv/bin/activate
```
- Setup project requirements 

```bash
pip install -U pip setuptools setuptools_scm tox
```
- Install 

```bash
pip install -e .
```

## Run tests 
(recommended)
```bash
tox
```
you can also use pytest directly 
First install this
```bash 
pip install pytest pytest-cov
```
then `pytest`

## Run api 
You just have to run main app with unicorn like
```bash
uvicorn main:app   --app-dir src/news_api --reload
```
You must choose the right directory ;)

Go to http://localhost:8000/docs to interact with the api
## Build docs
```bash
tox -e docs
```
html documentation is now available in  docs/_build/html.
You can open with your web browser.

<!-- pyscaffold-notes -->

## Note

This project has been set up using PyScaffold 4.1.1. For details and usage
information on PyScaffold see https://pyscaffold.org/.
