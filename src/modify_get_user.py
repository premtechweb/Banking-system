import json
from get_user_data import get_user_name, insert_user_data

def load_user_data(file_name="./database/user_data.json"):
    try:
        with open(file_name, "r") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return []

def find_user_by_account_num(account_num, user_data):
    for user in user_data:
        if user["account_num"] == account_num:
            return user
    return None

def modify_user_data(account_num, file_name="./database/user_data.json"):
    user_data = load_user_data(file_name)

    user_to_modify = find_user_by_account_num(account_num, user_data)

    if user_to_modify:
        print(f"User found with account number {account_num}.")
        print("Current user data:")
        print(json.dumps(user_to_modify, indent=4))

        # Modify user data
        new_fname = input("Enter new first name (press Enter to keep current): ")
        user_to_modify["fname"] = new_fname if new_fname else user_to_modify["fname"]

        new_lname = input("Enter new last name (press Enter to keep current): ")
        user_to_modify["lname"] = new_lname if new_lname else user_to_modify["lname"]

        new_age = input("Enter new age (press Enter to keep current): ")
        user_to_modify["age"] = int(new_age) if new_age else user_to_modify["age"]

        new_num = input("Enter new number (press Enter to keep current): ")
        user_to_modify["num"] = int(new_num) if new_num else user_to_modify["num"]

        new_district = input("Enter new district name (press Enter to keep current): ")
        user_to_modify["district"] = new_district if new_district else user_to_modify["district"]

        new_state = input("Enter new state name (press Enter to keep current): ")
        user_to_modify["state"] = new_state if new_state else user_to_modify["state"]

        # Save modified data back to the file
        with open(file_name, "w") as file:
            json.dump(user_data, file, indent=9)
        
        print("User data modified successfully.")
    else:
        print(f"User not found with account number {account_num}.")

if __name__ == "__main__":
    account_num_to_modify = int(input("Enter the account number of the user to modify: "))
    modify_user_data(account_num_to_modify)
