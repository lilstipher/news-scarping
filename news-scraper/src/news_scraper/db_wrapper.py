from pymongo import MongoClient
import logging

_logger = logging.getLogger(__name__)

class DbWrapper():
    def __init__(self,db_config,type:str=None) -> None:
        if type is None :
            self.client =  MongoClient(host=db_config["host"], port=db_config["port"])
            _logger.info("Db connection initialized")
        else :
            #TODO: Other db
            self.client =  MongoClient(host=db_config["host"], port=db_config["port"])
            _logger.info("Db connection initialized")