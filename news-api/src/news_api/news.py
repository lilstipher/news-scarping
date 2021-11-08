import datetime
import json
from os import symlink
from pydantic import BaseModel, EmailStr



class News(BaseModel):
    """News Class

        Args:
            website (str): news provider
            publication_date (datetime.datetime): article date
            url (str): article url
            category (str): article category
            title (str): article title
            content (str): article content
    """        
    website:str
    publication_date:str
    url :str
    category:str
    title:str
    content:str
