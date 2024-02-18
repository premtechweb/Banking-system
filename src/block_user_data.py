import json

def load_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def save_json(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def delete_user_by_account_num(file_path, account_num_to_delete):
    data = load_json(file_path)

    # Find and remove the user data with the specified account_num
    data = [user for user in data if str(user.get('account_num')) != str(account_num_to_delete)]

    save_json(file_path, data)

if __name__ == "__main__":
    file_path = '../database/user_data.json'

    # Get the account number to delete from user input or any other source
    account_num_to_delete = input("Enter the account number to delete: ")

    delete_user_by_account_num(file_path, account_num_to_delete)

    print(f"User data with account_num {account_num_to_delete} deleted successfully.")
