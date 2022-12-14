from flask import Flask, Response, request
from datetime import datetime
import json
from database_operations import DatabaseOperations
from flask_cors import CORS
import sys


# Create the Flask application object.
app = Flask(__name__)

CORS(app)


@app.get("/notify", methods=["POST"])
def get_comment_info():
    content_type = request.headers.get('Content-Type')
        if content_type == 'application/json':
            new_comment = request.json 
            blog_owner = new_comment["blog_owner"]
            comment_poster = new_comment["comment_poster"]
            print("server received blog owner and comment poster info")

    # DFF TODO Explain status codes, content type, ... ...
    result = Response(json.dumps(msg), status=200, content_type="application/json")

    return result


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=5015)