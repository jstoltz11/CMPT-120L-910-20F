from flask import Flask
from flask import render_template
import logging

app = Flask(__name__)


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

@app.route('/')
def index():
    app.logger.info('User is on the home page.')
    return render_template('index.html')

@app.route('/1')
def page1():
    app.logger.info('User is on page 1.')
    return render_template('page1.html')

@app.route('/2')
def page2():
    app.logger.info('User is on page 2.')
    return render_template('page2.html')

@app.route('/3')
def page3():
    app.logger.info('User is on page 3.')
    return render_template('page3.html')