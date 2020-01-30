# Import section
from flask import Blueprint, jsonify,abort,request,current_app,redirect,url_for,session
from app import celery
from app.models import db,User

# Initializing the blueprint
blueprint_users = Blueprint("users",__name__,url_prefix="/users")


#### Listing accounts
@blueprint_users.route("/create",methods=["POST"])
def create_user():

    # Initializing the user
    user = User()
    user.name = "Alexey Zelenkin"
    user.email = "azelenkin@yandex.ru"
    user.status = "Just created"

    # Adding user to the database
    db.session.add(user)
    db.session.commit()

    # Sending response
    return jsonify(user.as_dict())
