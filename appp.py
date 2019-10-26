from flask import Flask,render_template,request, send_file,redirect,session
from io import BytesIO
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint, exc
from models import FileContents,Validate
from sqlalchemy.orm import sessionmaker
import random

app=Flask(__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = "sqlite:///filebase.db"
app.secret_key = 'hey there'
db= SQLAlchemy(app)


@app.route('/')
def log():
	return render_template('login.html')



@app.route('/inners',methods=["POST"])
def inn_login():
	POST_USERNAME = str(request.form['uname'])
	POST_PASSWORD = str(request.form['psw'])
	print (POST_USERNAME +POST_PASSWORD)
	
	cur_user = Validate.query.filter_by(id=POST_USERNAME, pwd=POST_PASSWORD).first()
	if(cur_user is None):
		return "You have not registered"
	else:
		session["username"]  = POST_USERNAME
		return render_template("inners.html")
		return "You are now logged in and your id is " + str(session["username"])


@app.route('/index')
def index():
	cur_file = FileContents.query.filter_by(uid = session["username"]).first()
	if(cur_file is None):

		return render_template('index.html')
	else:
		return render_template('d.html')



@app.route('/logout')
def logout():
	session.pop('username', None)
	return render_template('login.html')

@app.route('/upload', methods = ["POST"])
def upl():
	file = request.files['inputFile']

	newFile = FileContents(id=random.randint(1, 100000000),uid=session["username"],data= file.read(), subid=random.randint(10, 1000000), expid=random.randint(10, 1000000))
	db.session.add(newFile)
	db.session.commit()
	return render_template('d.html')

@app.route('/makeuser',methods=["POST"])
def inn():
	POST_USERNAME = str(request.form['name'])
	POST_PASSWORD = str(request.form['password'])
	print (POST_USERNAME +POST_PASSWORD)
	
	student = Validate(id= POST_USERNAME,pwd=POST_PASSWORD)
	db.session.add(student)
	db.session.commit()
	return render_template('login.html')

	#return 'saved'+file.filename+' to database'
#@app.route('/downbutton')
#def down():
	#return render_template('d.html')
@app.route('/signup.html')
def ppp():
	return render_template('signup.html')
@app.route('/intro.html')
def introframe():
	return render_template('intro.html')
@app.route('/sub.html')
def introframe0():
	return render_template('sub.html')
@app.route('/sub1.html')
def introframe1():
	return render_template('sub1.html')
@app.route('/sub2.html')
def introframe2():
	return render_template('sub2.html')
@app.route('/sub3.html')
def introframe3():
	return render_template('sub3.html')
@app.route('/download',methods=["POST"])
def download():
	file_data = FileContents.query.filter_by(uid=session["username"]).first()
	return send_file(BytesIO(file_data.data),attachment_filename="download.pdf",as_attachment=True)

if __name__== '__main__':
	app.run (debug = True)
