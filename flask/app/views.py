from flask import Flask, render_template
from app import app

@app.route('/')
def hello_world():
    return "Hello World!"