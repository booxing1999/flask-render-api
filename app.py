from flask import Flask, request, jsonify
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)

# **🔹 Gmail SMTP 設定**
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
GMAIL_USER = "booxing1999@gmail.com"
GMAIL_PASSWORD = "fuckrex8787"  # **應用程式密碼**

# **🔹 發送 Email**
def send_email(to_email, subject, body):
    msg = MIMEMultipart()
    msg["From"] = GMAIL_USER
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "html"))

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # **啟用 TLS 加密**
        server.login(GMAIL_USER, GMAIL_PASSWORD)
        server.sendmail(GMAIL_USER, to_email, msg.as_string())
        server.quit()
        print(f"✅ 郵件發送成功：{to_email}")
    except Exception as e:
        print(f"❌ 郵件發送失敗: {e}")

# **🔹 Flask API 路由**
@app.route("/send_email", methods=["POST"])
def send_email_webhook():
    data = request.json
    email = data.get("email")
    token = data.get("token")

    if email and token:
        email_body = f"""
        <h2>📩 驗證您的電子信箱</h2>
        <p>請點擊下方連結完成驗證：</p>
        <a href="https://script.google.com/macros/s/YOUR_SCRIPT_ID/exec?token={token}&check=verify">
            ✅ 點這邊開通
        </a>
        """
        send_email(email, "📩 驗證您的電子信箱", email_body)
        return jsonify({"message": "Email sent"}), 200
    else:
        return jsonify({"error": "Missing email or token"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)
