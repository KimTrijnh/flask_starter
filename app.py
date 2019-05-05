from src import app

from flask import render_template, url_for, redirect
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True) 

