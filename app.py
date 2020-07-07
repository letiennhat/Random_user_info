from faker import Faker
from faker.providers import internet
import numpy as np
import json
import time
from flask import Flask, jsonify
fake = Faker('vi_VN')
fake.add_provider(internet)
app = Flask(__name__)

class Generation_info:
    def __init__(self,number):
        self.number = number
    def begin(self):
        names = []
        emails = []
        phone_numbers = []
        for i in range(self.number):
            
            name = fake.name()
            while 1:
                email = fake.simple_profile()['mail']
                phone_number = fake.phone_number()
                if email not in emails:
                    if phone_number not in phone_numbers:
                        emails.append(email)
                        names.append(name)
                        phone_numbers.append(phone_number)
                        break
                    else:
                        continue
                else:
                    continue
        dic = {}
        
        for i in range(len(names)):
            dic['user'+str(i)] = {'name': names[i],'email': emails[i],'phone number':phone_numbers[i]}
        dic_large = {str(time.localtime(time.time()).tm_mday)+'/'+\
                     str(time.localtime(time.time()).tm_mon)+'/'+ str(time.localtime(time.time()).tm_year):[dic]}
        return dic_large
    def printf(self):
        print(self.begin())
    def jsonload(self):
        json_strings = self.begin()
        with open('users.jon','a') as f:
            f.write(str(json_strings))
        return json_strings
    def name(date_,key):
        return self.begin()[date_][0][key]['name']
    def email(date_,key):
        return self.begin()[date_][0][key]['email']
    def phone_number(date_,key):
        return self.begin()[date_][0][key]['phone number']
class Server(Generation_info):
    def __init__(self,app):
        self.app = app
        #Generation_info.__init__(self,number)
    @app.route('/<int:name>',methods = ['GET','POST'])
    def index(name):
        GI = Generation_info(name)
        return jsonify(GI.jsonload())
    def run(self):
        self.app.run('0.0.0.0',port=80,debug=1)
if __name__=="__main__":
    server = Server(app)
    server.run()

         
