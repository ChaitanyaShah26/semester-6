from flask import Flask, jsonify
from rate_limiter import TokenBucket

app = Flask(__name__)

limiter = TokenBucket(capacity=5, refill_rate=1)

@app.route('/')
def home():
    if limiter.allow_request():
        return jsonify({"status": "Success", "message": "Request Allowed ✅"}), 200
    else:
        return jsonify({"status": "Fail", "error": "Too Many Requests ❌"}), 429

if __name__ == '__main__':
    print("Rate Limiter Server running on http://127.0.0.1:5000")
    app.run(debug=True, port=5000)