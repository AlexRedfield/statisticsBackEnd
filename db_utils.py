import json
import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import *

Base = declarative_base()


def ini_session():
    engine = create_engine(
        "mysql+pymysql://root:mysql877@localhost:3306/steam", encoding="utf-8"
    )
    # 创建DBSession类型
    db_session = sessionmaker(bind=engine)
    return db_session()


class QueryData:
    def __init__(self):
        self.conn = ini_session()

    def query_session(self):
        game_sessions = (
            self.conn.query(t_session)
            .filter(t_session.columns["app_id"] == "990080")
            .all()
        )
        # print([game_session['app_id'] for game_session in game_sessions])
        return [tuple(session) for session in game_sessions]

    def __del__(self):
        self.conn.close()


# 生成model代码 sqlacodegen --noconstraints --outfile=models.py mysql+pymysql://root:mysql877@localhost:3306/steam?charset=utf8

class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            print("MyEncoder-datetime.datetime")
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        if isinstance(obj, bytes):
            return str(obj, encoding='utf-8')
        if isinstance(obj, int):
            return int(obj)
        elif isinstance(obj, float):
            return float(obj)
        #elif isinstance(obj, array):
        #    return obj.tolist()
        else:
            return super(MyEncoder, self).default(obj)

if __name__ == "__main__":
    query = QueryData()
    print(query.query_session())