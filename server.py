from flask import Flask, render_template, request, url_for, redirect
import smtplib
from email.message import EmailMessage

app = Flask(__name__)
print(__name__)

@app.route('/')
def welcome():
	return render_template('index.html')

@app.route('/<string:page_html>')
def index(page_html):
	return render_template(page_html)

@app.route('/submit_form',methods=['POST','GET'])
def sent_mail():
	if request.method == 'POST':

		data = request.form.to_dict()
		mail = EmailMessage()
		mail['from'] = 'adityapythonsite@gmail.com'
		mail['to'] = 'adityam544@gmail.com'
		mail['subject']= data['subject']
		mail.set_content(str('[Email : ' + data['email']+'] [Subject : ' + data['subject'] + '] [Message : '+data['message']+']'))
		with smtplib.SMTP(host='smtp.gmail.com',port = 587) as smtp:
			smtp.ehlo()
			smtp.starttls()
			smtp.login('adityapythonsite@gmail.com','!Q@W#E$R%T')
			smtp.send_message(mail)
		print('email sent')
		return redirect('thankyou.html')
	else:
		return 'Somthing went wrong'
