from flask import Flask,request
from flask_cors import CORS

app=Flask(__name__)
CORS(app)


@app.route('/get-name',methods=['get'])
def fnGetName():
    return "srinu"


