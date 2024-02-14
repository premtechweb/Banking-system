#from src import get_user_data

from src.get_user_data import *

def main():

    user_data = get_user_name()
    insert_user_data(user_data)

    print("Data added successfully...")

main()

