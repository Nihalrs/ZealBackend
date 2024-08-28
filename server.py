from flask import jsonify, request, Flask
from database import *

app=Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to home page lyilbiyunl'

if __name__=='__main__':
    app.run()