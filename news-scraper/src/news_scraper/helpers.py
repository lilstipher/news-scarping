import yaml
import logging


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

        
def flatten(list_of_lists:list[list])-> list:
    """flatten list of lists

    Args:
        list_of_lists (list[list]): list of lists

    Returns:
        list: list
    """    
    return [item for sublist in list_of_lists for item in sublist]
