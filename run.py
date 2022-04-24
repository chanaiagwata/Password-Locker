#!/usr/bin/env python3.8
from user import User

def main():
    print("Hello welcome to Password Locker. What is your name?")
    user_name = input()
    
    print(f"Hello {user_name}. What would you like to do?") #the 'f' before the string means allows interpolation, i.e variables inside the curly brackets are read and replaced by their values
    print('/n')
    
    while True:
        print("Use these short codes: 'nu' -to create new account, 'lg' -to login into your account, 'ex' to exit password locker")
        short_code =input().lower()
        
        if short_code == 'nu':
            print("New Account")
            print("-"*10)
            print("username...")
            user_name_created = input()
            
            print("password...")
            user_password_created = input()
            
            print("confirm Password...")
            user_password_confirmed = input()
            
            while user_password_created != user_password_confirmed:  #To authenticate password
                print("password doesn't match! check and try again")
                print("enter password")
                user_password_created = input()
                print("confirm password")
                user_password_confirmed = input()
            else:
                print(f"impressive!, new account {user_name_created} created successfuly")
                print('/n')
                print("Login into your account")
                print("username")
                username_logged = input()
                print("password")
                password_logged = input()
                
            while (username_logged != user_name_created or password_logged != user_name_created):
                print("inavalid! password does not match the account, try again")
                print("username")
                username_logged = input()
                print("password")
                password_logged = input()
            else:
                print(f"Welcome {username_logged}, you've been logged in successfully")
                print('/n')
                
        elif short_code == 'lg':
            
