class User:
    '''
    Class that holds website and password data for the users
    '''
    lock_list = []
    def __init__(self,identity,data_id,website,weblogin,name):
        self.identitity = identity
        self.data_id = data_id
        self.website = website
        self.web_key = weblogin
        self.user_name = name
    
     def add_password(self):
        '''
        creating a method that stores the username for a user
        '''
        User.lock_list.append(self)