from flask_socketio import SocketIO , emit
from flask import render_template, Flask

from flask_ngrok import run_with_ngrok

app = Flask(__name__)
socketio = SocketIO(app)
run_with_ngrok(app)

@app.route("/")
def start_page():
    return render_template("index.html")

# Here client-message is the event where client sends data to Server
@socketio.on('client-message')
def printMessage(msg):

    # Dictionary data comes so we have to parse it to get the meaningful data from it
    print("Received Message: " + msg['data'])


if(__name__)=="__main__":
    app.run()


