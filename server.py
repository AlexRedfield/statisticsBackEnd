import json

from flask import Flask
from flask import request
from db_utils import QueryData, MyEncoder

app = Flask(__name__)

conn = QueryData()


@app.route("/session")
def get_session():
    data = conn.query_session()

    json_data = json.dumps(data, cls=MyEncoder, indent=4, ensure_ascii=False)
    return json_data


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=80)
