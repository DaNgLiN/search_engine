"""Search engine web server."""

import browseing
from flask import Flask, render_template, request

my_index = browseing.Index("large-sample")
app = Flask(__name__)

@app.route("/")
def root():
    return render_template("index.html")

@app.route("/search")
def search():
    q = request.args['q']
    results = my_index.search(q)
    return render_template("results.html", q=q, results=results)
