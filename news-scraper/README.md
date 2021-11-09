# news-scraper


## Description
A simple news scraper built with requests and beautiful soup (python 3.9)
There is only one scraper implemented now (Only for the `guardian`)

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

## Run the scraper 
### How it works 
This is a cli scraper which runs in command line.
So to do understand everything run :
```
  python -m news_scraper.run --help
```
By defaut the scraper will use the config file inside the config folder.
However you can use your own configuration file. Ex :
```
  python -m news_scraper.run --config /path/to/config.yaml
```

### Config file structure
First you need a configuration file like 

```yaml
configs:
  scrapers:
    guardian:
      scraping_dates:
        - "2021/10/7"
        - "2021/10/6"
      categories:
        - "world"
      limit: 1
  database:
    type: "mongodb"
    host: "localhost"
    port: 27017
```
### Run
WARN : YOU SHOULD HAVE A MONGODB INSTANCE RUNNING
In very verbose mode (DEBUG)
```
  python -m news_scraper.run -vv
```
In verbose mode (INFO)
```
  python -m news_scraper.run -v
```
You must choose the right directory ;)

## Build docs
```bash
tox -e docs
```
The html documentation is now available in  docs/_build/html.
You can open with your web browser.

<!-- pyscaffold-notes -->

## Note

This project has been set up using PyScaffold 4.1.1. For details and usage
information on PyScaffold see https://pyscaffold.org/.
