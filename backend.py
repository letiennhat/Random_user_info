from faker import Faker
from faker.providers import internet
import numpy as np
import sys
import json
import time
fake = Faker('vi_VN')
#Faker.seed(447)
fake.add_provider(internet)
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
    def name(key):
        return self.begin()[key]['name']
    def email(key):
        return self.begin()[key]['email']
    def phone_number(key):
        return self.begin()[key]['phone number']
