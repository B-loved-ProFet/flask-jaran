from flask import Flask
from flask_mailman import Mail, EmailMessage

app = Flask(__name__)

mail = Mail(app)
connection = Mail.get_connection()
connection.open()

email1 = EmailMessage(
    'Hello',
    'Body goes here',
    'lewyywel@gmail.com',
    ['urbanszymon13@gmail.com'],
    connection=connection,
)

email1.send()

@app.route('/')
def hello_world():
    return 'Hello, World!'