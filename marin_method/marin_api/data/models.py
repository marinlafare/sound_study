# DATA

from typing import Any
from sqlalchemy import Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Date, Integer, String, Float
from sqlalchemy.orm import relationship

BASE = declarative_base()

def to_dict(obj: BASE) -> dict[str, Any]:
    return {x.name: getattr(obj, x.name) for x in obj.__table__.columns}

class Song(BASE):
    __tablename__ = "song"
    id = Column(Integer, primary_key = True, unique = True, autoincrement=True)
    name = Column(String, nullable = False)
    url = Column(String, nullable = False)
class Pitch(BASE):
    __tablename__ = "pitch"
    id = Column(Integer, primary_key=True, unique = True, autoincrement=True)
    time = Column(Float, nullable = False)
    confidence = Column(Float, nullable = False)
    pitch = Column(Float, nullable = False)
    activation = Column(Float, nullable = False)
    
    song_id = Column(Integer, ForeignKey("song.id"))
    song = relationship(Song)
