import decimal
import json
import datetime

from flask.json.provider import DefaultJSONProvider
from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker
from models import *

Base = declarative_base()


def ini_session():
    engine = create_engine(
        "mysql://root:mysql877@localhost:3306/steam", encoding="utf-8"
    )
    # 创建DBSession类型
    db_session = sessionmaker(bind=engine)
    return db_session(), engine


class QueryData:
    def __init__(self):
        self.conn, self.engine = ini_session()

    def query_session(self, game_id: str):
        game_sessions = (
            self.conn.query(t_session)
            .filter(or_(t_session.columns["app_id"] == game_id, game_id is None))
            .all()
        )
        # print([game_session['app_id'] for game_session in game_sessions])
        return [tuple(row) for row in game_sessions]


    def query_game_time(self):
        game_time = self.conn.query(t_most_played_games).all()
        game_time_list = [
            [i[0] for i in game_time],
            [i[1] for i in game_time],
            [i[2] for i in game_time],
        ]
        game_reverse = [l[::-1] for l in game_time_list]
        return [tuple(row) for row in game_reverse]

    def query_game_time_format(self):
        game_time = self.conn.query(t_most_played_games).all()

        return [tuple(row) for row in game_time]


# 生成model代码 sqlacodegen --noconstraints --outfile=models.py mysql+pymysql://root:mysql877@localhost:3306/steam?charset=utf8


class MyEncoder(DefaultJSONProvider):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        if isinstance(obj, decimal.Decimal) or isinstance(obj, float):
            return float(obj)
        if isinstance(obj, bytes):
            return str(obj, encoding="utf-8")
        if isinstance(obj, int):
            return int(obj)
        # elif isinstance(obj, array):
        #    return obj.tolist()
        else:
            return super(MyEncoder, self).default(obj)


if __name__ == "__main__":
    query = QueryData()
    print(query.query_session())
