from flask import Flask, request, jsonify
import os
import requests

SERVICE_B_URL = os.getenv("SERVICE_B_URL", "http://service_b:5001")

app = Flask(__name__)

@app.route("/hello")
def hello():
    name = request.args.get("name", "anonymous")

    resp = requests.post(f"{SERVICE_B_URL}/log", json={"name": name})
    data = resp.json()

    return jsonify({
        "message": f"Привет, {name}",
        "log_id": data.get("log_id"),
        "total_requests": data.get("total_requests")
    })


@app.route("/health")
def health():
    return jsonify({"status": "ok", "service": "service_a"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
