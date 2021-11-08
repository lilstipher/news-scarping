import yaml
import logging
import sys


def get_config(_logger: logging.Logger, path:str)->dict:
    """get config file

    Args:
        _logger (logging.Logger): logger
        path (str): /path/to/config

    Returns:
        dict: config
    """
    #TODO: check config file    
    config = {}
    try:
        with open(path, "r") as stream:
            config = yaml.safe_load(stream)
            _logger.debug(config)
            return config
    except Exception as err:
        _logger.error("Cannot open config file. Reason: {}".format(err))
        exit(1)

        
def setup_logging(loglevel):
    """Setup basic logging

    Args:
      loglevel (int): minimum loglevel for emitting messages
    """
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(
        level=loglevel, stream=sys.stdout, format=logformat, datefmt="%Y-%m-%d %H:%M:%S"
    )

