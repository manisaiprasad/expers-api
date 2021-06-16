from flask import Flask, request, abort, jsonify
import os
from pipelines import pipeline

app = Flask(__name__)
nlp = None


@app.before_first_request
def nlpdefine():
    global nlp
    nlp = pipeline("question-generation")


@app.route('/hello')
def smile():
    return jsonify({'message': 'hello'})


@app.route('/api', methods=['POST'])
def api():
    body = request.get_json()
    text = body.get('text', None)

    response = nlp(text)
    return jsonify({
        'success': True,
        'apiresponse': response
    })
