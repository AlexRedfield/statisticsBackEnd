from flask import Flask, jsonify, request, Response
from flask_cors import CORS, cross_origin

from db_utils import QueryData, MyEncoder
from pathlib import Path

app = Flask(__name__)
app.json = MyEncoder(app)

conn = QueryData()

SCREENSHOT_FOLDER = 'D:\\Steam\\userdata\\100603213\\760'


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


@app.route("/image", methods=['post', 'get'])  # http://127.0.0.1/image?id=990080&name=20230212222319_1.jpg
def post_screenshots():
    filename = request.args.get('name')
    game_id = request.args.get('id')
    path = f"{SCREENSHOT_FOLDER}\\remote\\{game_id}\\screenshots\\{filename}"
    resp = Response(open(path, 'rb'), mimetype="image/jpeg")
    return resp

@app.route("/thumbnail", methods=['post', 'get'])  # http://127.0.0.1/thumbnail?name=20230212225138_1.jpg
def post_thumbnails():
    filename = request.args.get('name')
    game_id = request.args.get('id')
    path = f"{SCREENSHOT_FOLDER}\\remote\\{game_id}\\screenshots\\thumbnails\\{filename}"
    resp = Response(open(path, 'rb'), mimetype="image/jpeg")
    return resp


@app.route('/page')  # http://127.0.0.1/page?id=990080&date=20230212
@cross_origin()
def post_screenshot_filenames():
    game_id = request.args.get('id')
    date = request.args.get('date')
    folder = f"{SCREENSHOT_FOLDER}\\remote\\{game_id}\\screenshots"
    files = [(game_id,f.name) for f in Path(folder).glob(f"{date}*.jpg")]
    return jsonify(files)



if __name__ == "__main__":
    app.debug = True
    app.run(port=80)
