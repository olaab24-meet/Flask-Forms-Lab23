from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)
app.config['SECRET_KEY'] = 'super-secret-key'

username = "ola"
password = "123"
facebook_friends=["Lauren","Malak","Siwar", "George", "Fouad", "Meow"]

@app.route('/', methods=['GET', 'POST'])  # '/' for the default page
def login():
	
	if request.method == 'POST':
		un=request.form['username']
		pw=request.form['password']
		if un==username and pw==password:
			return redirect(url_for('home'))
		else:
			return render_template('login.html')
	else:     	
			return render_template('login.html')
  

@app.route('/home')
def home():
	return render_template('home.html')



if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)
