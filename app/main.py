from flask import Flask
  
app = Flask(__name__)
  
@app.route("/get-name",methods=["get"])
def getName():
    return "srinu"