from config import PORT, IP
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify('ok')

if __name__ == '__main__':
    app.run(port=PORT)
