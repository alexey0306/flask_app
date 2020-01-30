# Import section
from flask import Blueprint, jsonify,abort,request,current_app,redirect,url_for,session
from app import celery
from app.tasks.s3_tasks import create_file

# Initializing the blueprint
blueprint_tasks = Blueprint("tasks",__name__,url_prefix="/tasks")


#### Listing accounts
@blueprint_tasks.route("/start",methods=["GET"])
def start_task():
    result = create_file.apply_async(("asdasda","asdasdasdasdasd"),countdown=60)
    return jsonify(result.id)
