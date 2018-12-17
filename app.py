from flask import Flask, render_template, request, flash, redirect, url_for
import MySQLdb
db = MySQLdb.connect("localhost","dbuser","1qazXSW21@","webapp")
cursor = db.cursor()

app = Flask(__name__)
app.secret_key = "super secret key123"

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/SubmitMessage',  methods=['POST'])
def submit():
   if request.method == 'POST':
       message = request.form['message']
       cursor.execute("INSERT INTO posts (post) VALUES(%s)", (message,))
       db.commit()
       flash('Your message saved successfully')
       return render_template('result.html')
   else:
       pass

@app.route('/SearchMessage',  methods=['POST'])
def search():
   if request.method == 'POST':
       message = request.form['message']
       x = cursor.execute("SELECT * FROM posts WHERE post = (%s)",(message,))
       print(x)
       if int(x) > 0:
	    flash('Your message is already existing!')
       else:
	    flash('Your message deosnt existing!')
       return render_template('result.html')
   else:
       pass

@app.route('/ListMessage',  methods=['POST'])
def list():
       cursor.execute("SELECT * FROM posts")
       data = cursor.fetchall()
       for raw in data:
	    flash(raw[1])
       return render_template('result.html')

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0',port=8080)
