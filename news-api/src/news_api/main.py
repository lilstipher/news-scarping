from types import TracebackType
from news_api import news, helpers, db_wrapper
from news_api import __version__
from typing import Optional

from fastapi import FastAPI
import logging
import os

import news_api

app = FastAPI()


__author__ = "lilstipher"
__copyright__ = "lilstipher"
__license__ = "MIT"

_logger = logging.getLogger(__name__)

# db connection

try:
    # Open config
    config_path = os.path.dirname(os.path.abspath(__file__))
    default_conf = os.path.join(config_path, "config/config.yaml")
    config = helpers.get_config(_logger, default_conf)

    # db Conn
    db_conn = db_wrapper.DbWrapper(config["configs"]["database"]).client
    helpers.setup_logging(config["configs"]["logging"]["level"])
    news_db = db_conn.news
    news_collection = news_db.news
    _logger.info("Server configured")

except Exception as err:
    _logger.error("Db connection error. Reason : {}".format(err))
    quit()  # Exit if no db

BASE_PATH = "/api/v0"


@app.on_event("startup")
def startup_event():
    _logger.info(config)
    try:
        news_collection.create_index([('content', 'text')])
    except Exception as err:
        _logger.warn(err)


@app.get(BASE_PATH+"/version", response_model=dict)
async def get_version():
    return {"api": "news-api", "version": "{ver}".format(ver=__version__)}


@app.get(BASE_PATH+"/db/config", response_model=dict)
async def get_config():
    return config


@app.get(BASE_PATH+"/news/providers/{provider}", response_model=list[news.News])
async def get_all_news_by_provider(provider:str):
    news_list = [news_obj for news_obj in news_collection.find({'website':provider})]

    _logger.debug(news_list)
    return news_list

@app.get(BASE_PATH+"/news/all", response_model=list[news.News])
async def get_all_news():
    news_list = [news_obj for news_obj in news_collection.find({})]

    _logger.debug(news_list)
    return news_list

@app.get(BASE_PATH+"/news/search/all", response_model=list[news.News])
async def search_all_news( query: str):
    news_list = []
    if query :
        news_list = [news_obj for news_obj in news_collection.find({"$text": {"$search": query }})]

    _logger.debug(news_list)
    return news_list

