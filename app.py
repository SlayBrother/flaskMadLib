from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = "colby_is_cool69420"
debug = DebugToolbarExtension(app)


@app.route('/')
def home_click():
    return render_template('home.html')

@app.route('/input')
def input_section():
    return render_template('input.html')

@app.route('/complete')
def complete_section():
    place=request.args["place"]
    adjective=request.args["adjective"]
    noun=request.args["noun"]
    verb=request.args["verb"]
    plural=request.args["plural"]
    return render_template('complete.html', noun=noun, adjective=adjective, place=place, verb=verb, plural=plural)