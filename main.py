from flask import Flask,jsonify
from backend import Generation_info 

app = Flask(__name__)

class RunServer:
    global app
    #def __init__(self,port_)
    @app.route('/<int:name>',methods = ['GET','POST'])
    def index(name):
        GI = Generation_info(name)
        return jsonify(GI.jsonload())
        #return str(GI.jsonload())
    def run(self):
        app.run('0.0.0.0',port=8080,debug=1)
run = RunServer()
run.run()
               
