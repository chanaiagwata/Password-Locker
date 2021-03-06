from cgi import test
import unittest
from user import User
from user import Credentials

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the User class behaviors.
    
    Args:
    unittest.TestCase: TextCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up a method to run before each test cases.
        '''
        self.new_user = User ('chanaiagwata','268231') #create user object
    
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.user_name,"chanaiagwata")
        self.assertEqual(self.new_user.password,"268231")
    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved to the user list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)
    
class TestCredentials(unittest.TestCase):
    '''
     Test class that defines test cases for the User class behaviors.
    
    Args:
    unittest.TestCase: TextCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up a method to run before each test cases.
        '''
        self.new_credential = Credentials ("facebook", "chanaiagwata", "268231")
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credential.account,"facebook")
        self.assertEqual(self.new_credential.username,"chanaiagwata")
        self.assertEqual(self.new_credential.password,"268231")
    def test_save_credential(self):
        '''
         test_save_credential test case to test if the credential object is saved to the credential list
        '''
        self.new_credential.save_credential()
        self.assertEqual(len(Credentials.credentials_list),1)
    def tearDown(self):
        '''
        tearDown method that does clean up after test cases has run
        '''
        Credentials.credentials_list = [] 
    def test_save_multiple_accounts(self):
        '''
        test_save_multiple_account to check if we can save multiple user
        object to our credential_list
        '''
        self.new_credential.save_credential()
        test_credential = Credentials("Instagram","sophierose","123") #new credential
        test_credential.save_credential()
        self.assertEqual(len(Credentials.credentials_list),2)
    def test_delete_credential(self):
        '''
        to test if we can remove account from credential list.
        '''
        self.new_credential.save_credential()
        test_credential = Credentials ("Instagram","sophierose","123")
        test_credential.save_credential()
        self.new_credential.delete_credentials() #deleting credential object
        self.assertEqual(len(Credentials.credentials_list),1)
        
    def test_find_credential_by_name(self):
        '''
         test to check if we can find a contact by account name and display information
        '''
        self.new_credential.save_credential()
        test_credential = Credentials("Instagram", "Instagram", "123")
        test_credential.save_credential()
        
        found_credential = Credentials.find_credential_by_name("Instagram")
        self.assertEqual(found_credential.account,test_credential.account)
    
         
    def test_credential_exists(self):
        '''
        test to check if we can return a Boolean if we cannot find a credential in the credential list
        '''
        self.new_credential.save_credential()
        test_credential = Credentials ("Instagram","sophierose","123")

        test_credential.save_credential()
        credential_exists = Credentials.credential_exists("Instagram")
        self.assertTrue(credential_exists)
    def test_display_all_credentials(self):
        '''
        method that returns a list of all credentials saved
        '''
        
        self.assertEqual(Credentials.display_credentials(), Credentials.credentials_list)
    

if __name__ == "__main__":
    unittest.main()