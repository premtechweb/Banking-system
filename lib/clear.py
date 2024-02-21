import os
from lib.__import__ import *

def os_name():

    name = os.name
    if name == "nt":
        os.system("cls")
    else:
        os.system("clear")

os_name()

