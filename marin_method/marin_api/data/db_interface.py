# DATA
from typing import Any
from .engine import DBSession
from .models import BASE,to_dict

DataObject = dict[str, Any]
class DBInterface:
    def __init__(self, db_class:type[BASE]):
        self.db_class = db_class
    def create(self, data: DataObject) -> DataObject:
        session = DBSession()
        item: BASE = self.db_class(**data)
        session.add(item)
        session.commit()
        result = to_dict(item)
        session.close()
        return result
    def create_all(self, data: DataObject) -> DataObject:
        session = DBSession()
        item: BASE = [self.db_class(**song) for song in data]
        session.add_all(item)
        session.commit()
        session.close()
        return True