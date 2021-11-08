import pytest

from news_scraper.run import  main,logging


__author__ = "lilstipher"
__copyright__ = "lilstipher"
__license__ = "MIT"


def test_main(capsys):
  
    # capsys is a pytest fixture that allows asserts agains stdout/stderr
    # https://docs.pytest.org/en/stable/capture.html
    main(["-vv"])
    #captured = capsys.readouterr()
