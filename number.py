from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 's@54e236ecr8v0x8972f@#$5vs!$'

# When user loads page
@app.route("/")
def index():
	if not 'answer' in session:
		session['answer'] = random.randrange(1,101)
	print session['answer']
	return	render_template('index.html')

# What happens after the user chooses number
@app.route("/result", methods =["POST"])
def result():
	number = int(request.form['number']) #number is a variable, stored with the user-
										#-input, and type-cast into integer type.
	if number > session['answer']:
		session['message'] = "Too High!"

	elif number < session['answer']:
		session['message'] = "Too Low.."
	else:
		session['message'] = str(session['answer'])+' was the number!'
	return redirect ('/')

# What happens when the user resets the game upon winning
@app.route('/reset')
def reset():
	session.pop('message') #session is an object.
	session.pop('answer') #We pop the value paired to-
	return redirect("/") #-the key of "message" out of the object.

app.run(debug=True)
