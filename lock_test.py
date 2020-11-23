import unittest  # Importing the unittest module
from lock import User,Credentials
import pyperclip



class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the users class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_data = User(1, 1, "twitter.com", "steve99", "steve")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_data.identity,1)
        self.assertEqual(self.new_data.data_id,1)
        self.assertEqual(self.new_data.website,"twitter.com")
        self.assertEqual(self.new_data.weblogin,"steve99")
        self.assertEqual(self.new_data.name,"steve")

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.lock_list = []

    def test_save_password(self):
        '''
        test_save_password test case to test if the user object is saved into
         the lock list
        '''
        self.new_data.save_password()# saving the new password
        self.assertEqual(len(User.lock_list),1)

    def test_display_data(self):
        '''
        test_display_data to test if the data can be displayed.
        '''
        self.new_data.save_password()
        test_data = User(1, 1, "twitter.com", "steve99", "steve")
        test_data.save_password()

        data_found = User.display_data(1,1)
        self.assertEqual(data_found.website,test_data.website)


    def test_data_exist(self):
        '''
        test_data_exist to test if the function for checking data works
        '''
        self.new_data.save_password()
        test_data = User(1,1,"facebook.com","musky","tesla")
        test_data.save_password()

        data_exists = User.existing_data(1)
        self.assertTrue(data_exists)
    
    def test_copy_password(self):
        '''
        Test to confirm that we are copying the saved password from a found account
        '''
        self.new_data.save_password()
        #User.copy_password(1,1)

        self.assertEqual(self.new_data.weblogin,pyperclip.paste())


class TestCredentials(unittest.TestCase):
    
    '''
    Test class that defines test cases for the credentials class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = Credentials(1,"Steve99","stevo")


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.identify,1)
        self.assertEqual(self.new_user.user_name,"Steve99")
        self.assertEqual(self.new_user.password,"stevo")

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credentials.user_list = []

    def test_create(self):
        '''
       Test to check if the new credentials is saved into the list
        '''
        self.new_user.create_account()
        self.assertEqual(len(Credentials.user_list),1)
    
    def test_authenticate(self):
        '''
        Test to check if the authenticate function can sign in a user properly
        '''
        self.new_user.create_account()
        test_account = Credentials(1,"Test","Password")
        test_account.create_account()

        found_user = Credentials.authenticate_account("Test","Password")
        self.assertEqual(found_user.identify , test_account.identify)

if __name__ == '__main__':
    unittest.main()

