import datetime
import json


class News():
    def __init__(self, publication_date: datetime.datetime, url: str, category: str, title: str, content: str):
        
        formatted_datetime = publication_date.isoformat()
        self.publication_date =  json.dumps(formatted_datetime)
        self.url = url
        self.category = category
        self.title = title
        self.content = content
