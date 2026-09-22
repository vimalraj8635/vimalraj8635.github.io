from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import resend

app = Flask(__name__)

# Configure CORS explicitly for your frontend domain
CORS(app, resources={r"/*": {"origins": "https://vimalraj8635.github.io"}})

# Initialize Resend with your API Key env variable
resend.api_key = os.environ.get('MAIL_API_KEY') 

@app.route('/send-message', methods=['POST'])
def send_message():
    try:
        data = request.json
        name = data.get('name', '')
        email = data.get('email', '')
        message = data.get('message', '')

        if not name or not email or not message:
            return jsonify({"status": "error", "message": "All fields required"}), 400

        # Construct the email plain-text body
        email_body = f"""
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

        # Resend Free Tier rule: Sent from 'onboarding@resend.dev' to your verified account email
        params = {
            "from": "Portfolio Contact <onboarding@resend.dev>",
            "to": "vimalraj8635@gmail.com",
            "subject": f"📩 New Portfolio Message from {name}",
            "text": email_body
        }

        # Send using a standard HTTP request over HTTPS port 443
        resend.Emails.send(params)
        
        return jsonify({"status": "success", "message": "Email sent successfully!"})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run()
