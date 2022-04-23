class User:
    user_list = [] #Empty credential list
    '''
    class that generates new instances of user
    '''
    
    def __init__(self,user_name,password):
        '''
        __init__ method  helps define properties for the application
        '''
        self.user_name = user_name
        self.password = password
        
    def save_user(self):
        '''
        saves user object into the user_list
        '''
        
        User.user_list.append(self)