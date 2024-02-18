import json
import os


def load_json(file_path):
    abs_path = os.path.abspath(file_path)
    print("Attempting to load JSON from:", abs_path)
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def save_json(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def modify_user_data(file_path, account_num, new_balance):
    data = load_json(file_path)

    # Convert account_num to integer for comparison
    account_num = int(account_num)

    # Modify the user data
    for user in data:
        if user.get('account_num') == account_num:
            user['balance'] = new_balance
            break

    save_json(file_path, data)

