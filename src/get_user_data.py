import json

def get_user_name():

    try:

        global fname
        
        fname = input("Enter your first Name : ")
        lname = input("Enter your last Name : ")
        age = int(input("Enter your Age : "))
        num = int(input("Enter your Number : "))
        district = input("Enter your District name : ")
        state = input("Enter your State name : ")

    except ValueError:
        print("Kindly insert correct value!!! ")
    except UnboundLocalError:
        print("Kindly insert correct value!!! ")


    user_data = {
        "fname" : fname,
        "lname" : lname,
        "age" : age,
        "num" : num,
        "district" : district,
        "state" : state,
    }

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



