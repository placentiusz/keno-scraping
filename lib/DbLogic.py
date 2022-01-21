from typing import List

from sqlalchemy import engine
from sqlalchemy.orm import Session

import dblotto


class DBLogic:
    def __init__(self, config):
        self.engine = engine.create_engine(
            engine.url.URL(
                "mysql+mysqldb",
                username=config['mysql']['user'],
                password=config['mysql']['password'],
                host=config['mysql']['host'],
                database=config['mysql']['database'],
            )
        )

        # mapped classes are ready
        self.Result = dblotto.Result

    def check_and_update(self, results) -> int:
        list_to_insert = []
        for date, result, number in results:
            if not self.get_wynik_by_number(number):
                list_to_insert.append(dblotto.Result(Number=number, Date=date, Result=result, Game='Keno'))
        if len(list_to_insert) > 0:
            session = Session(self.engine)
            session.add_all(list_to_insert)
            session.commit()
            session.close()
        return len(list_to_insert)

    def get_wynik_by_number(self, number: int) -> List[dblotto.Result]:
        session = Session(self.engine)
        trytyty = session.query(self.Result).filter(self.Result.Number == number).first()
        return trytyty

