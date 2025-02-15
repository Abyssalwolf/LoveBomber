from flask import Flask, request, render_template, jsonify 
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send-email', methods=['POST'])
def send_email():
    data = request.get_json()
    message = data.get("message")

    if not message:
        return jsonify({"message": "Message cannot be empty"}), 400

    sender_email = "lovelettter4u@gmail.com"
    receiver_email = "lovelettter4u@gmail.com"
    password = "huiiucoccdedxbdp"  # Use your generated App Password

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = "Test Email"
    msg.attach(MIMEText(message, 'plain'))


    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        return jsonify({"message": "Love bomb sent successfully!"})
    except Exception as e:
        return jsonify({"message": f"Failed to send email: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)