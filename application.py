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

    return render_template("signin.html")

#@app.route("/<string:channel>")
#def channel(channel):
#    channel_name = request.form.get("channel_name")
#    flag = False
#    for item in channels:
#        if channel_name == item:
#            flag = True
#    if flag is False:
#        channels.append(channel_name)
#    else:
#        return render_template("error.html", message="This name of channel is not available")

#    return render_template("channel.html", channel=channel_name)
