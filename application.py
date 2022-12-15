from flask import Flask, Response, request
from datetime import datetime
import json
from database_operations import DatabaseOperations
from flask_cors import CORS
import sys


# Create the Flask application object.
app = Flask(__name__)

CORS(app)


@app.route("/notify", methods=["POST"])
def add_comment_info():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        new_comment = request.json 
        blog_id = new_comment["blog_id"]
        comment_poster = new_comment["comment_poster"]
        print("server received blog owner and comment poster info", blog_id, comment_poster)
    blog_owner, blog_title = DatabaseOperations.get_ownwer_id_and_blog_title(blog_id)
    result = DatabaseOperations.new_notification(blog_owner, comment_poster, blog_title)
    return result

@app.route("/countnotification", methods=["GET"])
def get_comment_info():
    username = request.args.get('username')
    count = DatabaseOperations.count_notification(username)
    print(count)
    return Response(str(count), status=200, content_type="application/json")

@app.route("/getnotificationinfo", methods=["GET"])
def get_notification_info():
    username = request.args.get('username')
    result = DatabaseOperations.comment_poster_and_blog_title_info(username)
    return result
    
@app.route("/removenotification", methods=["GET"])
def remove_notification():
    username = request.args.get('username')
    result = DatabaseOperations.remove_notification(username)
    return result

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=5015)
    