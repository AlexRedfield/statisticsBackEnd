import json

from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin
from db_utils import QueryData, MyEncoder

app = Flask(__name__)

conn = QueryData()


@app.route("/session")
@cross_origin()
def get_session():
    data = conn.query_session()

    json_data = json.dumps(data, cls=MyEncoder, indent=4, ensure_ascii=False)
    return json_data

@app.route("/playtime")
@cross_origin()
def get_playtime():
    data=conn.query_game_time()
    json_data = json.dumps(data, cls=MyEncoder, indent=4, ensure_ascii=False)
    return json_data


if __name__ == "__main__":
    app.debug = True
    app.run(port=80)
