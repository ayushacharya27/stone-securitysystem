import cv2
from flask import Flask , Response

from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)

@app.route("/")
def PrintMessage():
    return "Stone Security System"

if __name__ == "__main__":
    app.run()

 