from flask import Flask, request
from sender import send_email

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    # Usuario
    user = request.form['1']
    password = request.form['2']
    from_addr = user

    # SMTP server
    smtp_server = request.form['3']
    smtp_port = request.form['4']

    # Destinatario
    to_addrs = request.form['5']
    subject = request.form['6']
    # message = argv[7]
    message = ''

    send_email(user, password, from_addr, smtp_server, smtp_port, to_addrs, subject, message)

    return '{}\n{}'.format(user, password)

if __name__ == '__main__':
    app.run(debug=True)
