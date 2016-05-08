from flask import Flask, flash, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'secret_key11'


@app.route('/')
def index():
	session['randy'] = random.randrange(1,101)
	return render_template('index.html')
	

@app.route('/process', methods=['POST'])
def process():
	if request.method == 'POST':
		
		user_guess = int(request.form['guess'])
		if user_guess < int(session['randy']):
			return render_template('toolow.html')
		if user_guess > int(session['randy']):
			return render_template('toohigh.html')
		if user_guess == int(session['randy']):
			return render_template('correct.html')

@app.route('/rand', methods=['GET'])
def play():
	if request.method == 'GET':
		session.pop('randy')
		return redirect('/')
   # we'll talk about the following two lines after we learn a little more
   # about forms
  
  	
app.run(debug=True)

