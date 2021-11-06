import pytest

from news_scraper.guardian_scraper import *

__author__ = "lilstipher"
__copyright__ = "lilstipher"
__license__ = "MIT"


date = datetime.datetime.today()
x = GuardianScraper(date)
n = x.get_news()
print(n[0].__dict__)



