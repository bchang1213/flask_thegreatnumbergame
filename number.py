from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.secret_key = 's@54e236ecr8v0x8972f@#$5vs!$'

@app.route("")
def initialize():
	return	render_template('index.html')


app.run(debug=True)
