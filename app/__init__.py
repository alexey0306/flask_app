# Import section
import datetime,json
from flask import Flask,jsonify,request,render_template,send_from_directory
from app.config import DevelopmentConfig
from celery import Celery
from app.models import db

# Initializing the SocketIO and Celery
celery = Celery(__name__, broker=DevelopmentConfig.CELERY_BROKER_URL)

def create_app(object_name):
    app = Flask(__name__)
    app.config.from_object(object_name)
    db.init_app(app)
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask


    # Import blueprints
    from app.controllers.tasks import blueprint_tasks
    from app.controllers.users import blueprint_users

    # Registering blueprints
    app.register_blueprint(blueprint_tasks)
    app.register_blueprint(blueprint_users)

    @app.route('/')
    def index():
        return jsonify("Working")

    # Custom HTTP error handlers
    @app.errorhandler(400)
    def custom_400(error):
        return jsonify(message=error.description['message']),400

    @app.errorhandler(401)
    def custom_401(error):
        return jsonify(message=error.description['message']),401

    @app.errorhandler(403)
    def custom_403(error):
        return jsonify(message=error.description['message']),403

    @app.errorhandler(404)
    def custom_404(error):
        return jsonify(message="Item or resource not found"),404

    @app.errorhandler(405)
    def custom_405(error):
        return jsonify(message="Not allowed"),405

    @app.errorhandler(500)
    def custom_500(error):
        return jsonify(message=error.description['message']),500

    #@app.errorhandler(Exception)
    #def unhandled_exception(e):
    #    return jsonify(message=str(e)),500

    return app
