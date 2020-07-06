from faker import Faker
from faker.providers import internet
import numpy as np
import sys
import json
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
            while 1:
                name = fake.name()
                email = fake.simple_profile()['mail']
                phone_number = fake.phone_number()
                if name not in names :
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
                else:
                    continue
        #lists = [names,emails,phone_numbers]
        dic = {}
        for i in range(len(names)):
            dic['user'+str(i)] = {'name': names[i],'email': emails[i],'phone number':phone_numbers[i]}
        return dic
    def printf(self):
        print(self.begin())
    def jsonload(self):
        json_strings = self.begin()
        return json_strings
    def name(key):
        return self.begin()[key]['name']
    def email(key):
        return self.begin()[key]['email']
    def phone_number(key):
        return self.begin()[key]['phone number']
        
#X = Generation_info(2)
#print(X.jsonload())
#js = json.loads(json_strings)



