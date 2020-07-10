from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/<username>/<int:post_id>')
def hello_world(username=None,post_id=None):
   return render_template('index.html',name=username,post_id=post_id)

@app.route('/about.html')
def hello_about():
    return render_template('about.html')



@app.route('/blog/2020/dogs')
def hello_dogs():
    return 'Dogss!!!'