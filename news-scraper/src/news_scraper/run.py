"""
Then run ``pip install .`` (or ``pip install -e .`` for editable mode)
which will install the command ``fibonacci`` inside your current environment.

Besides console scripts, the header (i.e. until ``_logger``...) of this file can
also be used as template for Python modules.

References:
    - https://setuptools.readthedocs.io/en/latest/userguide/entry_point.html
    - https://pip.pypa.io/en/stable/reference/pip_install
"""

import argparse
import logging
import sys
import os
import datetime

from news_scraper import __version__

from news_scraper import db_wrapper
from news_scraper import guardian_scraper
from news_scraper import helpers

__author__ = "lilstipher"
__copyright__ = "lilstipher"
__license__ = "MIT"

_logger = logging.getLogger(__name__)


# ---- CLI ----
# The functions defined in this section are wrappers around the main Python
# API allowing them to be called directly from the terminal as a CLI
# executable/script.


def parse_args(args):
    """Parse command line parameters

    Args:
      args (List[str]): command line parameters as list of strings
          (for example  ``["--help"]``).

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    parser = argparse.ArgumentParser(description="Just a Fibonacci demonstration")
    parser.add_argument(
        "--version",
        action="version",
        version="news-scraper {ver}".format(ver=__version__),
    )
    parser.add_argument(
        "-v",
        "--verbose",
        dest="loglevel",
        help="set loglevel to INFO",
        action="store_const",
        const=logging.INFO,
    )
    parser.add_argument(
        "-vv",
        "--very-verbose",
        dest="loglevel",
        help="set loglevel to DEBUG",
        action="store_const",
        const=logging.DEBUG,
    )
    parser.add_argument(
        "-c",
        "--config",
        dest="config",
        help="set config file",
        type=str
    )
    return parser.parse_args(args)


def setup_logging(loglevel):
    """Setup basic logging

    Args:
      loglevel (int): minimum loglevel for emitting messages
    """
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(
        level=loglevel, stream=sys.stdout, format=logformat, datefmt="%Y-%m-%d %H:%M:%S"
    )


def main(args):
    """Wrapper allowing :func:`fib` to be called with string arguments in a CLI fashion

    Instead of returning the value from :func:`fib`, it prints the result to the
    ``stdout`` in a nicely formatted message.

    Args:
      args (List[str]): command line parameters as list of strings
          (for example  ``["--verbose", "confi.yaml"]``).
    """
    args = parse_args(args)
    setup_logging(args.loglevel)
    # Open config file
    if args.config:
        config = helpers.get_config(_logger, args.config)
    else:
        config_path = os.path.dirname(os.path.abspath(__file__))
        default_conf = os.path.join(config_path, "config/config.yaml")
        config = helpers.get_config(_logger, default_conf)
    
    #Connect to db

    try:
        db_conn = db_wrapper.DbWrapper(config["configs"]["database"]).client
    except Exception as err:
        _logger.error("Db connection error. Reason : {}".format(err))
        exit(1) #Exit if no db

    # load guardian scraper
    if config["configs"]["scrapers"]["guardian"]:
        #Load config
        guardian = config["configs"]["scrapers"]["guardian"]
        dates = guardian.get('scraping_dates', None)
        if dates is None:
            _logger.warn("No dates, using current date")
            date = datetime.datetime.today()
            date = date.replace(minute=0, hour=0, second=0)
            dates = [ date ]
        else :
            dates = [ datetime.datetime.strptime(date.strip(), '%Y/%m/%d') for date in dates]

        _logger.info("scraping_dates: {}".format(dates))

        categories = guardian.get('categories', None)
        _logger.info("categories: {}".format(categories))

        limit = guardian.get('limit', None)
        _logger.info("limit = {}".format(limit))

        #Scrap data
        guardian_scrapers_list = [ guardian_scraper.GuardianScraper(date,categories) for date in dates]
        guardian_news = helpers.flatten([ scraper.get_news(limit=limit) for scraper in guardian_scrapers_list])
        _logger.debug("Some news ? {}".format(guardian_news[0].__dict__))
        
        # Store news 

        news_db = db_conn.news
        news_collection = news_db.news
        for news in guardian_news:
            check = news_collection.find_one({ "publication_date": news.publication_date,"url":news.url })
            if not check: #save if dont exists
                news_collection.insert_one(news.__dict__)
                _logger.info(check)
            else : 
                _logger.info("These news already scraped")


    _logger.info("Good Bye")


def run():
    """Calls :func:`main` passing the CLI arguments extracted from :obj:`sys.argv`

    This function can be used as entry point to create console scripts with setuptools.
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    # ^  This is a guard statement that will prevent the following code from
    #    being executed in the case someone imports this file instead of
    #    executing it as a script.
    #    https://docs.python.org/3/library/__main__.html

    # After installing your project with pip, users can also run your Python
    # modules as scripts via the ``-m`` flag, as defined in PEP 338::
    #
    #     python -m news_scraper.run -vv
    #
    run()
