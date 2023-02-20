from flask import Flask, render_template, redirect, url_for, request,send_from_directory
import os
import numpy as np

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def layout():
  return render_template('index.html')

@app.route('/widgets')
def widgets():
  return render_template('pages/widgets.html')


if __name__ == '__main__':
  app.run(host='127.0.0.1', port=5000, debug=True)
#app.run(host='0.0.0.0', port=8080)