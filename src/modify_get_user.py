import json
from get_user_data import *

def validate_data():

        fnames = input("Enter Your first name : ")
        lname = input("Enter Your second name : ")

        if fnames == get_user_name(fname):
                print("valid")
        else:
                print("Invalid") 

validate_data()


