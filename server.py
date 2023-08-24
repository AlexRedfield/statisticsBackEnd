from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin


from db_utils import QueryData, MyEncoder


app = Flask(__name__)
app.json = MyEncoder(app)

conn = QueryData()


@app.route("/session")
@cross_origin()
def get_session():
    game_id = request.args.get("id")
    data = conn.query_session(game_id)
    return data

@app.route("/playtime")
@cross_origin()
def get_playtime():
    data = conn.query_game_time()
    return jsonify(data)


@app.route("/re_playtime")
@cross_origin()
def get_re_playtime():
    data = conn.query_game_time_format()
    return jsonify(data)


if __name__ == "__main__":
    app.debug = True
    app.run(port=80)

