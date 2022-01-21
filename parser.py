import configparser

from lib.DbLogic import DBLogic
from lib.Scrap import Scrap


class Parser:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        url = config['web']['keno']
        results = Scrap(url)
        base = DBLogic(config)
        print(f'Inserted rows: %s' % base.check_and_update(results.get_keno_data()))


if __name__ == "__main__":
    # execute only if run as a script
    Parser()

