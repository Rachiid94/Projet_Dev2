from interface_kivy.verifications import *


class UnknownMode(Exception):
    pass


def register():
    email = input("What's your email ?")
    pseudo = input("What's your pseudo ?")
    password = input("What's your password ?")
    confirm_password = input("Confirm password ?")

    # Function for register


def login():
    pseudo = input("What's your pseudo ?")
    password = input("What's your password ?")
    user_in_bdd(pseudo, password)


def ilc_launcher():
    mode = input("Do you want to login or register ?")
    if mode == "register":
        register()
    elif mode == "login":
        login()
    else:
        raise UnknownMode("Mode known: login or register")

