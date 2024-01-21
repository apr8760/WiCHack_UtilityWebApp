from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

# set up application
app = Flask(__name__)

# create index route so that when we browse to url we don't immediatly 404
@app.route("/")
# define function for that route
def index():
  return render_template('index.html')

# run app and if come across problem show us
if __name__ == "__main__":
  app.run(debug=True)