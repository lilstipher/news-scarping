import pytest
from fastapi.testclient import TestClient
import news_api as api
from news_api.main import app

__author__ = "lilstipher"
__copyright__ = "lilstipher"
__license__ = "MIT"

client = TestClient(app)

BASE_PATH = "/api/v0"
def test_version():
    response = client.get(BASE_PATH + "/version")
    assert response.status_code == 200
    assert response.json() == {"api": "news-api", "version": "{ver}".format(ver=api.__version__)}

def test_get_all_news():
    response = client.get(BASE_PATH + "/news/all")
    assert response.status_code == 200
    assert isinstance (response.json(),list)
