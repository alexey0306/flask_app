from flask_script import Manager, Server
from app import create_app
from flask_migrate import Migrate, MigrateCommand
from app.models import db

# Creating SSL context
#context = ('server.crt', 'server.key')

# Creating the app
flask_app = create_app('app.config.DevelopmentConfig')
migrate = Migrate(flask_app, db)
manager = Manager(flask_app)
#manager.add_command("server", Server(ssl_crt="server.pem",ssl_key="server.key",host="0.0.0.0",threaded=True))
manager.add_command("server",Server(host="0.0.0.0",threaded=True))
manager.add_command('db', MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app=flask_app,db=db)

if __name__ == "__main__":
	manager.run()
