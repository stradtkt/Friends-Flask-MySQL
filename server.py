from flask import Flask, request, redirect, render_template, session, flash, url_for
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'friends')
@app.route('/')
def index():
	query = "SELECT * FROM `friends`.`users`;"
	users = mysql.query_db(query)
	return render_template('index.html', users=users)

@app.route('/add')
def add():
  return render_template('add-friends.html')

@app.route('/add-friends', methods=['POST'])
def add_friends():
  	valid = True
	if request.form['first_name'] == "":
  		valid = False
		flash("First name cannot be blank")
	if request.form['last_name'] == "":
  		valid = False
		flash("Last name cannot be blank")
	if request.form['occupation'] == "":
  		valid = False
		flash("Occupation cannot be blank")
	if valid != True:
  		return redirect("/")
	else:
  	  	query = "INSERT INTO `friends`.`users` (`first_name`, `last_name`, `occupation`, `created_at`, `updated_at`) VALUES (:first_name, :last_name, :occ, now(), now());"
      	data = {
        	"first_name": request.form['first_name'],
        	"last_name": request.form['last_name'],
        	"occ": request.form['occupation']
      	}
    	mysql.query_db(query, data)
	return redirect('/')
	

app.run(debug=True)