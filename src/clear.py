import os

def os_name():

    name = os.name
    if name == "nt":
        os_name()
    else:
        os.system("clear")

os_name()