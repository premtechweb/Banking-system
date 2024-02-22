import json
import random
import datetime
from lib.__import__ import *
from lib.color import *


def get_user_name():

    dt = datetime.datetime.now()

    try:

        user_data = {}     
        user_data["account_num"] = random.randint(1,10000000000)   
        user_data['fname'] = input("Enter your first Name : ")
        user_data["lname"] = input("Enter your last Name : ")
        user_data["age"] = int(input("Enter your Age : "))
        user_data["num"] = int(input("Enter your Number : "))
        user_data["district"] = input("Enter your District name : ")
        user_data["state"] = input("Enter your State name : ")
        user_data["balance"] = input("Enter your Amount : ")
        user_data["Date"] = dt.strftime("%d-%m-%Y")
        user_data["Time"] = dt.strftime("%H:%M:%S")

    except ValueError:
        print("Kindly insert correct value!!! ")
    except UnboundLocalError:
        print("Kindly insert correct value!!! ")

    return user_data

def insert_user_data(user_data, file_name="./database/user_data.json"):

    try:
        with open(file_name, "r") as file:
            data = json.load(file)
    
    except FileNotFoundError:
        data = []

    data.append(user_data)

    with open(file_name, "w") as file:
        json.dump(data, file, indent=9)

    return file_name



