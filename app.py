from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_worl():
    return 'Hello World'
@app.route('/test')
def test1():
    return 'test to see'

