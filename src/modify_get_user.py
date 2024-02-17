import json


def load_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def save_json(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def modify_user_data(file_path, account_num, new_fname):
    data = load_json(file_path)

    # Modify the user data
    for user in data:
        if account_num_to_update == account_num:
            user['fname'] = new_fname
            break
        else:
            print("Data not found")

    save_json(file_path, data)

if __name__ == "__main__":
    file_path = '../database/user_data.json'

    account_num_to_update = input("Enter the account number to update: ")
    
    print("1.) First Name")
    print("2.) Last Name")
    print("3.) Age")
    print("4.) Number")
    print("5.) District")
    print("6.) State")
    
    modify = input("Which data if you want to change enter number : ")

    if modify == "1" :
        new_fname = input("Enter the new first name : ")
    elif modify == 2 :
        new_lname = input("Enter the new last name : ")
    elif modify == 3 :
        new_age = input("Enter the new Age : ")
    elif modify == 4 :
        new_num = input("Enter the new Number : ")
    elif modify == 5 :
        new_district = input("Enter the new District : ")
    elif modify == 3 :
        new_state = input("Enter the new State : ")
    else:
        print("Invalid input!!!")



    modify_user_data(file_path, account_num_to_update, modify_data)

    print(f"User data for account_num {account_num_to_update} updated successfully.")
