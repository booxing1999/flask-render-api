from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Render!"

@app.route("/send_email", methods=["POST"])
def send_email():
    data = request.json
    email = data.get("email")
    token = data.get("token")

    if email and token:
        print(f"📩 發送郵件給 {email}，驗證碼 {token}")
        return jsonify({"message": "Email sent"}), 200
    else:
        return jsonify({"error": "Missing email or token"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)