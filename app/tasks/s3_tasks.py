# Import section
from app import celery
import time,datetime
from app.models import db,User

# Defining the tasks
@celery.task(bind=True)
def create_file(self,id,bucket,path):
    #time.sleep(5)

    # Updating user data
    user = User.query.filter_by(id=id).first()

    if not user:
        return {
            "status": "error",
            "finished": time.time(),
            "error": "User not found"
        }

    # Updating user's data
    user.status = "Updated information on %s" % (str(datetime.datetime.now()))

    # Commiting the transaction
    db.session.commit()

    # Sending response
    return {
        "status": "ok",
        "finished": time.time(),
        "error": ""
    }

