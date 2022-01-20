import configparser
from  lib.Scrap import  Scrap

class Parser:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        url = config['web']['keno']
        result = Scrap(url)
        result.getData()


if __name__ == "__main__":
    # execute only if run as a script
    Parser()

