from flask import Flask, request
import requests

app = Flask("$")

@app.route("/")
def hello():
    requests.post("http://127.0.0.1:6120/callback", json={"data": request.json, "id": "$"})
    return 200