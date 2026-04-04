from flask import Flask, render_template, request, jsonify
from model import predict_attack
import csv
import os
import pandas as pd
from datetime import datetime

app = Flask(__name__)

LOG_FILE = "user_logs.csv"

def init_log_file():
    with open(LOG_FILE, "w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
        writer.writerow(["timestamp", "duration", "protocol", "src_bytes", "dst_bytes", "result", "confidence"])

if not os.path.exists(LOG_FILE):
    init_log_file()

def read_logs():
    if not os.path.exists(LOG_FILE):
        return pd.DataFrame(), 0, 0
    try:
        df = pd.read_csv(LOG_FILE)
    except Exception:
        init_log_file()
        return pd.DataFrame(), 0, 0

    if df.empty:
        return df, 0, 0

    if "timestamp" not in df.columns:
        df.insert(0, "timestamp", "—")
    if "confidence" not in df.columns:
        df["confidence"] = "—"

    normal = len(df[df["result"] == "normal"])
    attack = len(df[df["result"] == "attack"])
    return df, normal, attack


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    confidence = None
    logs = []

    if request.method == "POST":
        duration = int(request.form["duration"])
        protocol = request.form["protocol"]
        src = int(request.form["src"])
        dst = int(request.form["dst"])

        result, confidence = predict_attack(duration, protocol, src, dst)

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if os.path.exists(LOG_FILE):
            try:
                existing = pd.read_csv(LOG_FILE)
                if list(existing.columns) != ["timestamp", "duration", "protocol", "src_bytes", "dst_bytes", "result", "confidence"]:
                    init_log_file()
            except Exception:
                init_log_file()

        with open(LOG_FILE, "a", newline="") as f:
            writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
            writer.writerow([timestamp, duration, protocol, src, dst, result, confidence])

    df, normal, attack = read_logs()
    if not df.empty:
        logs = df.tail(50).values.tolist()[::-1]

    return render_template("index.html",
                           result=result,
                           confidence=confidence,
                           logs=logs,
                           normal=normal,
                           attack=attack,
                           total=normal + attack)


@app.route("/api/stats")
def api_stats():
    df, normal, attack = read_logs()
    if df.empty:
        return jsonify({"normal": 0, "attack": 0, "total": 0, "protocol_dist": {}, "timeline": [], "src_stats": {}})

    try:
        proto_dist = df.groupby(["protocol", "result"]).size().unstack(fill_value=0).to_dict()
    except Exception:
        proto_dist = {}

    timeline = []
    if "timestamp" in df.columns:
        timeline = df.tail(20)[["timestamp", "result", "confidence"]].to_dict(orient="records")

    try:
        src_stats = df.groupby("result")["src_bytes"].mean().to_dict()
        src_stats = {k: round(v, 1) for k, v in src_stats.items()}
    except Exception:
        src_stats = {}

    return jsonify({
        "normal": int(normal),
        "attack": int(attack),
        "total": int(normal + attack),
        "protocol_dist": proto_dist,
        "timeline": timeline,
        "src_stats": src_stats
    })


@app.route("/api/clear", methods=["POST"])
def clear_logs():
    init_log_file()
    return jsonify({"status": "cleared"})


if __name__ == "__main__":
    app.run(debug=True)