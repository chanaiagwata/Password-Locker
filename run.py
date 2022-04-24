#!/usr/bin/env python3.8
from user import Credentials, User

def create_user(username, password):
    '''
    function to create a new user
    '''
    new_user = User(username,password)
    return new_user
def save_user(user):
    '''
    function to save a user
    '''
    user.save_user()
def del_user(user):
    '''
    function to delete user
    '''
    user.delete_contact()
def verify_user(username,password):
    '''
    function that checks if user exists before creating credential
    '''
    check_user = Credentials.verify_user(username,password)
    return check_user
def create_credential(account,username,password):
    '''
    function that creates new user instance for user object
    '''
    new_credential = Credentials(account,username,password)
    return new_credential
def save_credential(credential):
    '''
    function that saves new credential
    '''
    Credentials.save_credential(credential)
    
def display_credential(username):
    '''
    function to display saved usercredential
    '''
    return Credentials.display_credentials(username)

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
                
            while (username_logged != user_name_created or password_logged != user_password_created):
                print("inavalid! password does not match the account, try again")
                print("username")
                username_logged = input()
                print("password")
                password_logged = input()
            else:
                print(f"Welcome {username_logged}, you've been logged in successfully, choose an option to continue")
                print('/n')
                
        elif short_code == 'lg':
            print("welcome!")
            print("Enter username")
            login_username = input()
            print("Enter password")
            login_password = input()
            print('/n')
            
            while login_username != username_logged or login_password != password_logged:
                print("Invalid username or password") 
                print("Enter user name")
                login_username = input()
                print("Enter Password")
                login_password = input()
                print("/n")
            else:
                print("Welcome! You've been logged in successfully, choose an option to continue")
                print('/n')
            
            
            
        elif short_code == 'ex':
            print("Bye...")
            break
        else:
            print("Wrong input. Please use the short codes")
            
            
            
            
            
            
            
if __name__ == '__main__':
    main()
            
