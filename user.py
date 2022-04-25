import string
from ast import Return
from operator import truediv
# from turtle import clear



class User:
    user_list = [] #Empty credential list
    '''
    class that generates new instances of user
    '''
    
    def __init__(self,user_name,password):
        '''
        __init__ method  helps define user properties for the application
        '''
        self.user_name = user_name
        self.password = password
        
    def save_user(self):
        '''
        saves user object into the user_list
        '''
        
        User.user_list.append(self)
        
    def delete_user(self):
        '''
        delete_user method deletes saved user credential from the user list.
        '''
        User.user_list.remove(self)
    
    @classmethod
    def display_user(cls):
        '''
        display_user method that returns the contact list
        '''
        return cls.user_list
    
class Credentials:
    '''
    class that generates new instances of Credentials
    '''
    credentials_list = []
    @classmethod
    def verify_user(cls,username,password):
        '''
        method that checks if a user exists from the user list
        Args:
        username:name to search if it exists  
        password:passwod to search if it exists.
        Returns: Boolean, returns True or False depending on whether the username or password exist    
        '''
        
        user_exists =""
        for user in User.user_list:
            if(user.username == username and user.password == password):
                user_exists ==user.username
        return user_exists
    def __init__(self,account,username, password ):
        '''
        __init__method defines credential properties for to be saved
        '''
        self.account = account
        self.username = username
        self.password = password
    def save_credential(self):
        '''
        save_credential method that saves credential added to credential list
        '''
        Credentials.credentials_list.append(self)
    def delete_credentials(self):
        '''
        delete_credential method to delete credential from credential list
        '''
        Credentials.credentials_list.remove(self)
   
    @classmethod
    def credential_exists(cls, account):
        '''
        method that checks if credential exists
        Args:
            account:account
        Return:
            Boolean: True or False dependening if the credential exists
        '''
        for credential in cls.credentials_list:
            if credential.account == account:
                return credential
       
    def find_credential_by_name(cls, account):
        '''
        find_credential method that searches credentials by account_name.
        Args:
            acount:account 
        Returns: Credential of user that matches the account
        '''
        for credential in cls.credentials_list:
            if credential.account == account:
                return credential

    @classmethod
    def display_credentials(cls):
        '''
        display_credentials method lists all properties in the credential list  
        '''
        return cls.credentials_list
    