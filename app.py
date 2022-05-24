# import flask and all of its modules
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, make_response, session, g, abort, send_from_directory, send_file, Response, stream_with_context
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/<filename>')
def send_static(filename):
    return send_from_directory('static', filename)
if __name__ == '__main__':
    app.run(debug=True)
    