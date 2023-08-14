# coding: utf-8
from sqlalchemy import Column, DECIMAL, DateTime, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class GameInfo(Base):
    __tablename__ = 'game_info'

    id = Column(Integer, primary_key=True)
    app_id = Column(String(256), nullable=False)
    name = Column(String(256), nullable=False)


t_last_7_days = Table(
    'last_7_days', metadata,
    Column('app_id', String(256)),
    Column('name', String(256)),
    Column('sum', DECIMAL(32, 0))
)


t_most_played_games = Table(
    'most_played_games', metadata,
    Column('app_id', String(256)),
    Column('name', String(256)),
    Column('sum', DECIMAL(32, 0))
)


t_session = Table(
    'session', metadata,
    Column('app_id', String(256)),
    Column('name', String(256)),
    Column('start_time', DateTime),
    Column('end_time', DateTime),
    Column('duration', Integer)
)


class SteamSession(Base):
    __tablename__ = 'steam_sessions'

    id = Column(Integer, primary_key=True)
    app_id = Column(String(256), nullable=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    duration = Column(Integer, nullable=False)


t_this_month = Table(
    'this_month', metadata,
    Column('app_id', String(256)),
    Column('name', String(256)),
    Column('sum', DECIMAL(32, 0))
)
