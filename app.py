from flask import Flask, render_template, jsonify, request
from name import find_name, is_name
from nlp_fin import rest

import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import names
from nltk.corpus import stopwords
import json
import math
import re
from nltk.tokenize import sent_tokenize, word_tokenize

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/change_name', methods=['POST'])
def requester():
	if request.json:
		json = request.get_json(silent=True)
		print(json)
		text = json["text"]
		name = find_name(text)
		data = jsonify({'name': name})
		print(text)
		return data


@app.route('/api/check_name', methods=['POST', 'GET'])
def checker():
	if request.json:
		json = request.get_json(silent=True)
		print(json)
		text = json["name"]
		result = is_name(text)
		print(result)
		if(result):
			return("1")
		else:
			return("0")

@app.route('/result', methods=['POST', 'GET'])
def result() :
	if request.method == 'POST' :
		word = str(request.form['text']).lower()
		print(word)
		fin = rest(word)
		print(str(fin))
		return str(fin)
		# rest(word)"ram with 4gb and budget with 12000rs."
			
if __name__ == '__main__':
    app.run()
