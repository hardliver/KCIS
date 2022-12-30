from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
   return 'HELLO'

@app.route('/a/<name>')
def a(name=None):
   return render_template('index.html', name123=name)

if __name__ == '__main__':
	app.run('0.0.0.0', debug=True)
