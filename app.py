from flask import Flask, request, redirect
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.debug = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
@app.route('/')
def index():
	profiles = Profile.query.all()
	return render_template('index.html', profiles=profiles)


if __name__ == '__main__':
	app.run()


























from flask_migrate import Migrate, migrate








migrate = Migrate(app, db)

class Profile(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(20), unique=False, nullable=False)
	last_name = db.Column(db.String(20), unique=False, nullable=False)
	age = db.Column(db.Integer, nullable=False)


	def __repr__(self):
		return f"Name : {self.first_name}, Age: {self.age}"









@app.route('/add_data')
def add_data():
	return render_template('add_profile.html')


@app.route('/add', methods=["POST"])
def profile():

	first_name = request.form.get("first_name")
	last_name = request.form.get("last_name")
	age = request.form.get("age")

	if first_name != '' and last_name != '' and age is not None:
		p = Profile(first_name=first_name, last_name=last_name, age=age)
		db.session.add(p)
		db.session.commit()
		return redirect('/')
	else:
		return redirect('/')




@app.route('/delete/<int:id>')
def erase(id):
	

	data = Profile.query.get(id)
	db.session.delete(data)
	db.session.commit()
	return redirect('/')


