
from lib.__import__ import *

def main():

    os_name()

    try:
        print(f"{green}1.) New User")
        print(f"{green}2.) Existing User")
        print(f"{green}3.) Deposit")
        print(f"{red}4.) Exit")

        choice = int(input(f"{blue}Enter Your Option : "))

        if choice == 1:        
            user_data = get_user_name()
            insert_user_data(user_data)

            print("Data added successfully...")

        elif choice == 2:
            os_name()
            print("Existing User...")

            print("1.) My Account")
            print("2.) My Balance")
            print("3.) Account Modify")
            print("4.) Account Block")
            print("5.) Back")

            ex_user = int(input("Enter Your Options : "))

            if ex_user == 1:
                print("My Account")
                account_number_to_search = int(input("Enter your Account Number : "))
                json_file_path = "./database/user_data.json"

                get_user_data_by_account_number(account_number_to_search, json_file_path)

            elif ex_user == 2:
                print("My Balance")
                account_number_to_search = int(input("Enter your Account Number : "))
                json_file_path = "./database/user_data.json"

                get_balance_by_account_number(account_number_to_search, json_file_path)

            elif ex_user == 3:
                print("Account Modify")
                if __name__ == "__main__":
                    file_path = './database/user_data.json'

                    account_num_to_update = input("Enter the account number to update: ")

                    new_fname = input("Enter the new first name: ")
                    new_lname = input("Enter the new last name: ")
                    new_age = input("Enter the new age: ")
                    new_num = input("Enter the new number: ")
                    new_district = input("Enter the new district: ")  # Fix the typo here
                    new_state = input("Enter the new state: ")
                    
                    modify_user_data(file_path, account_num_to_update, new_fname, new_lname, new_age, new_num, new_district, new_state)

                    print(f"User data for account_num {account_num_to_update} updated successfully.")

            elif ex_user == 4:
                print("Account Block")
                                
                file_path = './database/user_data.json'

                # Get the account number to delete from user input or any other source
                account_num_to_delete = input("Enter the account number to delete: ")

                delete_user_by_account_num(file_path, account_num_to_delete)

                print(f"User data with account_num {account_num_to_delete} deleted successfully.")

            elif ex_user == 5:
                main()

        elif choice == 3:
            print("Deposit...")
            
            file_path = './database/user_data.json'

            account_num_to_update = input("Enter the account number to update: ")
            new_balance = input("Enter the Balance : ")
                
            modify_user_data(file_path, account_num_to_update, new_balance)

            print(f"User data for account_num {account_num_to_update} updated successfully.")

        elif choice == 4:
            print("Exiting...")
            exit()

        else:
            print("Invalid!!!")
    
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
    except KeyboardInterrupt:
        print("\nExiting...")
        exit()
    except EOFError:
        print("Exiting..")
        exit()

if __name__ == "__main__":
    main()
