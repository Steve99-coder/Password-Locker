class User:
    '''
    Class that generates new instances of users
    '''
    lock_list = [] # Empty lock list

    def __init__(self,identity,data_id,website,weblogin,name):
        self.identity = identity
        self.data_id = data_id
        self.website = website
        self.weblogin = weblogin
        self.name = name


    def save_password(self):

        '''
        save_password method saves user objects into lock_list
        '''

        User.lock_list.append(self)
    
    @classmethod
    def display_data(cls,number,count):
        '''
        display all passwords generated by the user
        '''
        for password in cls.lock_list:
            if password.identity == number:
                if password.data_id == counter:
                    return password
    
   