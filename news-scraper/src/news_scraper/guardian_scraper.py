import datetime
import requests
import logging
from bs4 import BeautifulSoup
import re
from . import news

_logger = logging.getLogger(__name__)


class GuardianScraper ():
    def __init__(self, date: datetime.datetime, categories: list = None):
        """[summary]

        Args:
            date (datetime.date): [description]
            categories (list, optional): [description]. Defaults to None.
        """        
        if categories is None:
            self.categories = ["world"]
            _logger.info('Set default category for GuardianScraper')
        elif isinstance(categories, list):
            self.categories = categories
        self.date = date
        self.categories_urls = {}
        self.articles_urls = { }

        self.BASE_URL = 'https://www.theguardian.com'
        self.news = []
        _logger.info('GuardianScraper configured')

    def _generate_urls(self):
        """ generate category base urls
        """        
        date_str = self.date.strftime("%Y/%b/%d").lower()
        self.categories_urls = { category:'{}/{}/{}/all'.format(self.BASE_URL,category,date_str) for category in self.categories }
    
    def _fetch_articles_urls(self,limit:int=None):
        """ Fetch articles urls

        Args:
            limit (int, optional): limit number of urls per category. Defaults to None.
        """
        use_limit =False
        if limit and isinstance(limit, int):
            use_limit =True
        else :
            _logger.info('Skipping Limit')
        
        for category,urls in self.categories_urls.items():
            try:
                response = requests.get(urls)
                #print(response.text)
                soup = BeautifulSoup(response.text, 'html.parser')
                links = [ a['href'] for a in soup.find_all(href=re.compile(urls[:-3])) ] # href like https://www.theguardian.com/us-news/2021/nov/06/*
                if use_limit :
                    self.articles_urls[category] = links[:limit]
                else:
                    self.articles_urls[category] = links
                _logger.info("fetch_articles_urls")
            except Exception as err :
                _logger.error(err)



    def get_news(self,limit:int=None) -> list[news.News]:
        """ Get news form the guardian

        Args:
            limit (int, optional): limit numbers of news. Defaults to None.

        Returns:
            list[news.News]: list of news objects
        """        

        self._generate_urls()
        _logger.debug(self.categories_urls)
        self._fetch_articles_urls(limit=limit)
        _logger.debug(self.articles_urls)
        #filter
        responses = []
        for category,urls in self.articles_urls.items():
            for url in urls:
                try:
                    response = requests.get(url)
                    soup = BeautifulSoup(response.text, 'html.parser')
                    title = soup.title.text 
                    content = soup.find_all(id="maincontent")[0].text
                    news_obj = news.News("guardian",self.date,url,category,title,content)
                    responses.append(news_obj)
                    _logger.debug("Got news for {}".format(url))
                except Exception as err :
                    _logger.error(err)
        return responses

