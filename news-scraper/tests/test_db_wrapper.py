from news_scraper import db_wrapper
import pytest
import os
from news_scraper.helpers import *
_logger = logging.getLogger(__name__)

def test_db_connection():
    config_path = os.path.dirname(os.path.abspath(__file__))
    config = get_config(_logger, os.path.join(config_path, "config/config.yaml"))
    db_wrapper_obj = db_wrapper.DbWrapper(config["configs"]["database"])
    assert db_wrapper_obj.client.HOST == "localhost"
    assert db_wrapper_obj.client.PORT == 27017
