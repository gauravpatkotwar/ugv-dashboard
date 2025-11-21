from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode="eventlet")

@app.route("/")
def index():
    tunnel_url = "https://rover.your-domain.com"
    return render_template("index.html", tunnel=tunnel_url)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=10000)
