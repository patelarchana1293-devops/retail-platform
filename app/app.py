from flask import Flask, jsonify
import os

app = Flask(__name__)

VERSION = os.getenv("APP_VERSION", "4.2.0")
HEALTH_STATUS = os.getenv("HEALTH_STATUS", "healthy")


@app.route("/")
def home():
    return jsonify({
        "application": "Retail Platform",
        "version": VERSION,
        "status": "running"
    })


@app.route("/health")
def health():
    if HEALTH_STATUS != "healthy":
        return jsonify({
            "status": "unhealthy",
            "version": VERSION
        }), 500

    return jsonify({
        "status": "healthy",
        "version": VERSION
    }), 200


@app.route("/payment")
def payment():
    return jsonify({
        "status": "success",
        "message": "Payment processed successfully",
        "version": VERSION
    }), 200

@app.route("/products")
def products():
    return jsonify({
        "products": [
            "Laptop",
            "Mobile",
            "Headphones"
        ],
        "version": VERSION
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)