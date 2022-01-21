# coding: utf-8
from sqlalchemy import Column, DateTime, Index, String, Text
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Result(Base):
    __tablename__ = 'results'
    __table_args__ = (
        Index('Id', 'Id', 'Number'),
    )

    Id = Column(INTEGER(11), primary_key=True)
    Number = Column(INTEGER(11), nullable=False)
    Date = Column(DateTime, nullable=False, index=True)
    Game = Column(String(100), nullable=False)
    Result = Column(Text, nullable=False)
