from flask_mail import Mail, Message

app = Flask(__name__)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = "jhsm9534"
app.config['MAIL_PASSWORD'] = 'zkjhs9534'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

@app.route("/email", methods=['post', 'get'])
def email_test():
    if request.method == 'POST':
        senders = request.form['email_sender']
        receiver = request.form['email_receiver']
        content = request.form['email_content']
        receiver = receiver.split(',')
       
        for i in range(len(receiver)):
            receiver[i] = receiver[i].strip()
           
        print(receiver)
 
        result = send_email(senders, receiver, content)
      
        if not result:
            return render_template('email.html', content="Email is sent")
        else:
            return render_template('email.html', content="Email is not sent")
       
    else:
        return render_template('email.html')
   
def send_email(senders, receiver, content):
    try:
        mail = Mail(app)
        msg = Message('Title', sender = senders, recipients = receiver)
        msg.body = content
        mail.send(msg)
    except Exception:
        pass
    finally:
        pass

   