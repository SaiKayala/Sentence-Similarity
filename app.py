### Flask web application for sentence similarity ###
from flask import Flask, request, render_template
import urllib.request
import requests
import json

# App config.
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def homePage():
    return render_template('home.html')


@app.route('/query', methods=['GET', 'POST'])
def query():
	url = 'https://pwqfi9ur44.execute-api.us-east-2.amazonaws.com/test1/newtest11'
	data = {"doc1": request.form['document_1'], "doc2": request.form['document_2']}
	r = requests.post(url, json=data)
	return render_template('output.html', Cosine_Score = float(r.content))
if __name__ == "__main__":
  app.run()
