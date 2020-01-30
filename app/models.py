# Import section
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Models
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255),default='',nullable=False,index=True)
    email = db.Column(db.String(255),default='',nullable=False)
    status = db.Column(db.String(512),default="",nullable=True)

    def __init__(self):
    	pass

    def __repr__(self):
    	return "<User, name=%r, email=%r>" % (self.name,self.email,self.subject)

    def update(self,data):
        if "name" in data:
            if data['name'] != "":
                self.name = data['name']
        if "email" in data:
            if data['email'] != "":
                self.email = data['email']
        if "subject" in data:
            if data['subject'] != "":
                self.subject = data['subject']

    def as_dict(self):
        user =  {c.name: getattr(self, c.name) for c in self.__table__.columns}
        #user.pop('password')
        return user
