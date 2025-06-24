from flask import Flask, render_template, request, redirect, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'AIzaSyAwN-2gwOAJNsErb3irP2-nR7Ug1499fHE'

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'aniqafarhan31@gmail.com'   
app.config['MAIL_PASSWORD'] = 'xiow qilc ddid zbrl'
app.config['MAIL_DEFAULT_SENDER'] = 'your_email@gmail.com'

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    msg = Message(f'New Contact from {name}',
                  recipients=['aniqafarhan31@gmail.com']) 
    msg.body = f"From: {name}\nEmail: {email}\n\nMessage:\n{message}"
    mail.send(msg)

    flash('Message sent successfully!')
    return redirect('/')
