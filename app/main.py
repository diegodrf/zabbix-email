from flask import Flask, request, jsonify
from sender import send_email
import json

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    # Usuario
    user = request.form['2']
    password = request.form['3']
    from_addr = user

    # SMTP server
    smtp_server = request.form['4']
    smtp_port = request.form['5']

    # Destinatario
    to_addrs = request.form['6']
    subject = request.form['7']
    message = request.form['8']

    try:
        send_email(user, password, from_addr, smtp_server, smtp_port, to_addrs, subject, message)
        status = {'status': 'OK'}
    except Exception as error:
        status = {'status': 'Fail', 'message': error}
    finally:
        return jsonify(json.dumps(status))

if __name__ == '__main__':
    app.run(debug=True)