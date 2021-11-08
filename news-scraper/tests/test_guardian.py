from news_scraper.news import News
import pytest

from news_scraper.guardian_scraper import *

__author__ = "lilstipher"
__copyright__ = "lilstipher"
__license__ = "MIT"



def test_guardian_defaut_ok():
    date = datetime.datetime(2021,11,8)
    x = GuardianScraper(date)
    n = x.get_news(limit=1)
    assert len(x.articles_urls["world"]) == 1
    assert len(n) == 1
    assert  isinstance(n[0], News)
    assert n[0].website == "guardian"

def test_guardian_category_ok():
    date = datetime.datetime(2021,11,8)
    x = GuardianScraper(date,categories=["world"])
    n = x.get_news(limit=2)
    assert len(x.articles_urls["world"]) == 2
    assert len(n) == 2
    assert  isinstance(n[0], News)
    assert n[0].website == "guardian"



