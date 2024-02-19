import json

def get_balance_by_account_number(account_number, json_file_path):
    with open(json_file_path, 'r') as file:
        data = json.load(file)

        for user in data:
            if user.get('account_num') == account_number:
                balance = user.get('balance')
                if balance is not None:
                    print(f"The balance for account number {account_number} is: {balance}")
                    return
                else:
                    print(f"Balance not found for account number {account_number}")
                    return

        print(f"User not found with account number {account_number}")

# Example usage

