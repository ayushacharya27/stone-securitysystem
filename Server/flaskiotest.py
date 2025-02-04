from flask_socketio import SocketIO , emit
from flask import render_template, Flask

from flask_ngrok import run_with_ngrok

app = Flask(__name__)
socketio = SocketIO(app)
run_with_ngrok(app)

@app.route("/")
def start_page():
    return render_template("index.html")

@socketio.on('client-message')
def printMessage(msg):
    print("Received Message: " + msg['data'])


if(__name__)=="__main__":
    app.run()


