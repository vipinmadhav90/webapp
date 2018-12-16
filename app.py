from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/SubmitMessage',  methods=['POST'])
def submit():
   if request.method == 'POST':
       message = request.form['message']
       return render_template('success.html', message=message)
   else:
       pass

@app.route('/SearchMessage',  methods=['POST'])
def search():
   if request.method == 'POST':
       message = request.form['message']
       return render_template('result.html', message=message)
   else:
       pass

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)
