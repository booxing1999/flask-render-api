from flask import Flask, request, jsonify
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

app = Flask(__name__)

# **🔹 Gmail SMTP 設定**
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
GMAIL_USER = os.getenv("GMAIL_USER")  # ✅ 從環境變數讀取
GMAIL_PASSWORD = os.getenv("GMAIL_PASSWORD")  # ✅ 從環境變數讀取


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
       <body style="font-family: Arial, sans-serif; background-color: #f4f4f4; color: #333; line-height: 1.6; text-align: center; padding: 20px; margin: 0;">
    <div style="max-width: 600px; background: #ffffff; padding: 20px; margin: 0 auto; border-radius: 10px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);">
        <h1 style="color: #d32f2f;">拳擊智多星®歡迎您！</h1>
        <p>感謝您報名領取 <strong>《拳擊學習大地圖》+《腳步指南》+《秘籍包》</strong>！💪🏆</p>
        <p>這些價值 <strong>899 美金</strong> 的學習資源，已經幫助無數專業選手與拳擊愛好者提升訓練效果。</p>
        
        <p>請點擊下方按鈕完成驗證，以確保您的電子信箱正確無誤：</p>
        
        <a href="https://script.google.com/macros/s/AKfycbzPzC_y6vCuvrQTTAZLKNIZFYxLm5ZW5ezkuNzTU3YfE7QEgfveaj7VpKd-06WAJho5/exec?token={token}&check=verify" 
           style="display: inline-block; background: #d32f2f; color: #ffffff; text-decoration: none; font-size: 18px; padding: 12px 20px; border-radius: 5px; margin-top: 20px; font-weight: bold;">
            ✅ 點這邊開通
        </a>

        <p><strong>⚠️ 注意：</strong></p>
        <ul style="text-align: left; display: inline-block; padding: 0; list-style: none;">
            <li style="margin-bottom: 8px;">🔹 此驗證連結僅限 <strong>30分鐘內有效</strong>，請盡快完成驗證！</li>
            <li style="margin-bottom: 8px;">🔹 驗證成功後，您將立即收到專屬的拳擊學習資源！</li>
            <li style="margin-bottom: 8px;">🔹 限量 <strong>200 份</strong>，送完即止！請把握機會！</li>
        </ul>

        <p>如果您沒有申請這份免費資料包，請忽略此封信。</p>

        <div style="margin-top: 20px; font-size: 14px; color: #777;">
            <p>📍 <strong>Instagram：</strong> <a href="https://www.instagram.com/booxing_1999/" target="_blank" style="color: #d32f2f; text-decoration: none;">@booxing_1999</a></p>
            <p>📍 <strong>官方網站：</strong> 拳擊智多星</p>
            <p><strong>拳擊智多星 團隊 敬上</strong></p>
        </div>
    </div>
</body>
        """
        send_email(email, "📩嗨！驗證您的電子信箱～", email_body)
        return jsonify({"message": "Email sent"}), 200
    else:
        return jsonify({"error": "Missing email or token"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)
