from flask import Flask, request, jsonify

app = Flask(__name__)

logs = []
counter = 0


@app.route("/log", methods=["POST"])
def log():
    global counter
    data = request.get_json() or {}
    name = data.get("name", "unknown")

    counter += 1
    log_item = {"id": counter, "name": name}
    logs.append(log_item)

    return jsonify({
        "log_id": log_item["id"],
        "name": name,
        "total_requests": counter
    })


@app.route("/logs")
def get_logs():
    return jsonify(logs)


@app.route("/health")
def health():
    return jsonify({"status": "ok", "service": "service_b"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
