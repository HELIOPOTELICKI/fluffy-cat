from flask import Flask, jsonify, request
import numpy as np
import openai
import urllib
import cv2
import os


openai.api_key = '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'
openai.Model.list()

def getRandomCat():
    response = openai.Image.create(
    prompt="Centered cat",
    n=1,
    size="512x512",
    )

    return response['data'][0]['url']

app = Flask(__name__)

@app.route('/random-cat', methods=['GET'])
def getCat():
    return jsonify({'url': getRandomCat()})

@app.route('/test', methods=['GET'])
def test():
    return jsonify({'test': 'test'})

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')