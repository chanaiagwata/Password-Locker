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
        self.new_credential = Credentials ("facebook" "chanaigwata", "268231")
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credential.account,"facebook")
        self.assertEqual(self.new_credential.username,"chanaiagwata")
        self.assertEqual(self.new_credential.password,"268231")





if __name__ == "__main__":
    unittest.main()