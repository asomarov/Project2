import os

from flask import Flask, session, render_template, request, jsonify
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

channels = []
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signin", methods=["POST"])
def signin():
    username = request.form.get("username")

    return render_template("signin.html", channels=channels)

@app.route("/create_channel", methods=["POST"])
def create_channel():
    channel_name = request.form.get("channel_name")
    flag = False
    for item in channels:
        if channel_name == item:
            flag = True
    if flag is False:
        channels.append(channel_name)
    else:
        return render_template("error.html", message="This name of channel is not available")

    return render_template("channel_succes.html", message="Your channel has been created", channel_name=channel_name)

@app.route("/signin/<string:channel_name>")
def channel(channel_name):
    return render_template("channel.html", channel=channel_name)

@socketio.on("/signin/<string:channel_name>send message")
def message(data):
    message = data["message"]
    emit("announce message", {"message": message}, broadcast=True)
