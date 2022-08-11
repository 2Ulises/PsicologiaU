from distutils.log import debug
from flask import flask,render_template
app= flask("ulises")

@app.route("/")
def hello_world():
    return "hello world"


