import json
import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_crypto():
    response = requests.get("https://api.coinpaprika.com/v1/tickers/dai-dai")
    crytpo_dai = json.loads(response.text)
    return render_template("index.html", crypto=crytpo_dai)

if __name__ == "__main__":
    app.run(debug=True)
