from flask import Flask, request, jsonify
from flask_mail import Mail, Message
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow requests from your portfolio frontend

# ── Gmail SMTP Configuration ──
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'vimalraj8635@gmail.com'   # Your Gmail
app.config['MAIL_PASSWORD'] = 'gyqo qkps djxd dadr'   # Gmail App Password (NOT real password)

mail = Mail(app)

@app.route('/send-message', methods=['POST'])
def send_message():
    try:
        data = request.json
        name    = data.get('name', '')
        email   = data.get('email', '')
        message = data.get('message', '')

        if not name or not email or not message:
            return jsonify({"status": "error", "message": "All fields required"}), 400

        msg = Message(
            subject=f"📩 New Portfolio Message from {name}",
            sender=app.config['MAIL_USERNAME'],
            recipients=['vimalraj8635@gmail.com']   # Where you receive the email
        )

        msg.body = f"""
You received a new message from your portfolio website!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━
👤 Name    : {name}
📧 Email   : {email}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💬 Message:
{message}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Sent from: vimalraj.dev portfolio
        """

        mail.send(msg)
        return jsonify({"status": "success", "message": "Email sent successfully!"})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)
