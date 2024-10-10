import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome!"

@app.route('/1')
def hello1():
    return 'This is Path 1?'

@app.route('/2')
def hello2():
    return 'This is Path 2?'

@app.route('/3')
def hello3():
    return 'This is Path 3?'

if __name__ == "__main__":
    app.run()
