from flask import Flask 
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = "sqlite:///filebase.db"
db= SQLAlchemy(app)

class Validate(db.Model):
	__tablename__ = 'validate'
	id = db.Column(db.Integer,primary_key=True)
	pwd = db.Column(db.String(20),nullable=False)
	#FileContents = db.relationship('FileContents', primaryjoin='validate.id==FileContents.user_id', lazy='dynamic')


class FileContents(db.Model):
	__tablename__ = 'FileContents'
	id = db.Column(db.Integer,primary_key=True)
	uid = db.Column(db.Integer,db.ForeignKey("validate.id"),nullable=False)
	data =db.Column(db.LargeBinary)
	subid =db.Column(db.Integer)
	expid = db.Column(db.Integer)
	__table_args__ = (
        db.PrimaryKeyConstraint('id', 'subid','expid'),
        {},
    )
db.create_all()