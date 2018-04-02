from flask import render_template
from AdminMateus import app


@app.route('/')
def index():
    return render_template('principal.html', titulo='Admin')