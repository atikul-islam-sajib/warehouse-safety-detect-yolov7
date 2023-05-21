import os
import flask

app=Flask(__name__)

@app.route("/")
def main():
    return "My First Image!!!"


@app.route("/container")
def hello():
    return "Container Working Successfully...."

if __nmae__=="__main__":
    app.run()