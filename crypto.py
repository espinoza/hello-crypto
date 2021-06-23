import time
import requests
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

@app.route("/")
def hello_crypto():
    """Create static html."""
    url = "https://api.coinpaprika.com/v1/tickers/dai-dai"
    crypto_dai = requests.get(url).json()
    return render_template("index.html", crypto=crypto_dai)

@socketio.on('start')
def handle_start():
    """Update html every 1 second."""
    while True:
        url = "https://api.coinpaprika.com/v1/tickers/dai-dai"
        crypto_dai = requests.get(url).json()
        print("Updating...")
        emit('update', crypto_dai)
        time.sleep(1)

if __name__ == "__main__":
    socketio.run(app)
