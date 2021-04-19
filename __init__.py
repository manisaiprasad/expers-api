from flask import Flask, request, abort, jsonify
import os
from . import pipelines

app = Flask(__name__)

nlp = pipelines.pipeline("multitask-qa-qg", model="valhalla/t5-base-qa-qg-hl")


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
