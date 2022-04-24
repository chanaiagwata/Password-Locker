#!/usr/bin/env python3.8
from user import User

def main():
    print("Hello welcome to Password Locker. What is your name?")
    user_name = input()
    
    print(f"Hello {user_name}. What would you like to do?")
    print('/n')
    
    while True:
        print("Use these short codes: 'nu' -to create new account, 'lg' -to login into your account, 'ex' to exit password locker")
        short_code =input().lower()
        
        if short_code == 'nu':
            print("New Account")
            print("-"*10)
            print("username...")
            user_name_created = input()
            
            print("Password...")
            user_password_created = input()
            
            print("Confirm Password...")
            user_password_confirmed = input()
            
            