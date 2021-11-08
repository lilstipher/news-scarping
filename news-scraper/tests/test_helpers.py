from news_scraper.helpers import *
import logging
import pytest
import os
_logger = logging.getLogger(__name__)


def test_load_guardian_conf():
    config_path = os.path.dirname(os.path.abspath(__file__))
    config = get_config(_logger, os.path.join(config_path, "config/config.yaml"))
    assert len(config["configs"]) == 2
    assert config["configs"]["scrapers"]["guardian"]['scraping_dates'] == [
        '2021/10/7', '2021/10/6']


def test_bad_conf_file():
    with pytest.raises(SystemExit):
        config = get_config(_logger, "g.yaml")
