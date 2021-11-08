import datetime
import json


class News():
    def __init__(self, website:str,publication_date: datetime.datetime, url: str, category: str, title: str, content: str):
        """News Class

        Args:
            website (str): news provider
            publication_date (datetime.datetime): article date
            url (str): article url
            category (str): article category
            title (str): article title
            content (str): article content
        """        
        self.website=website
        formatted_datetime = publication_date.isoformat()
        self.publication_date =  formatted_datetime
        self.url = url
        self.category = category
        self.title = title
        self.content = content
