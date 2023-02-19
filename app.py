from flask_cors import CORS
from flask import Flask, render_template, request
import smtplib
from email.message import EmailMessage
import ssl

app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/sent', methods=['POST'])
def sent():
    while True:
        receiver_email = request.form.get('email')
        try:
            receiver_message = request.form.get('messages')
            receiver_subject = request.form.get('subject')

            smtp_server = 'smtp.gmail.com'
            port = 465
            sender_email = "chitturisaikiran1210@gmail.com"
            password = "yndebnsjkvzvzksk"
            message = message = 'Hi ' + str(receiver_email) + \
                ', Thanks for visiting my Portfolio. Thank You  for your Message and i will look into it soon! \nyours faithfully,\n Sai Kiran.'

            msg = EmailMessage()
            msg.set_content(message)
            msg['Subject'] = "Kiran_Portfolio"
            msg['From'] = sender_email
            msg['To'] = receiver_email

            context = ssl.create_default_context()

            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, password)
                server.send_message(msg)

            msg1 = EmailMessage()
            msg1.set_content(receiver_message)
            msg1['Subject'] = receiver_subject
            msg1['From'] = sender_email
            msg1['To'] = "chitturidurgasatyasaikiran@gmail.com"

            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, password)
                server.send_message(msg1)
            return render_template('sent.html')

        except smtplib.SMTPRecipientsRefused as e:
            error_message = "The recipient's email address was refused by the server."
            print(error_message)
            return render_template('error.html', error=error_message)
        except smtplib.SMTPAuthenticationError as e:
            error_message = "There was an error while trying to authenticate with the email server."
            print(error_message)
            return render_template('error.html', error=error_message)
        except smtplib.SMTPException as e:
            error_message = "There was an error while sending the email."
            print(error_message)
            return render_template('error.html', error=error_message)


if __name__ == "__main__":
    app.run(debug=True)
