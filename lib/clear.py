import os
from lib.__import__ import *

def os_name():

    name = os.name
    if name == "nt":
        os.system("cls")
        print("Windows")
    else:
        os.system("clear")
        print("Linux")

os_name()

