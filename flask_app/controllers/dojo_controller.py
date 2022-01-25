from flask import Flask, render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods = ['POST'])
def process():
    if not Dojo.validator(request.form):
        return redirect('/')
    created_id = Dojo.create(request.form)
    return redirect(f'/result/{created_id}')

@app.route('/result/<int:dojo_id>')
def result(dojo_id):
    dojo = {
        "id": dojo_id
    }
    return render_template('result.html', dojo = Dojo.get_one(dojo))

@app.route('/return')
def go_back():
    return redirect('/')
