import json
from lib.__import__ import *

def get_user_data_by_account_number(account_number, json_file_path):
    with open(json_file_path, 'r') as file:
        data = json.load(file)

        for user in data:
            if user.get('account_num') == account_number:
                print(f"User data for account number {account_number}:")
                for key, value in user.items():
                    print(f"{key}: {value}")
                return

        print(f"User not found with account number {account_number}")

