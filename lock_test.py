import unittest  # Importing the unittest module
from lock import User


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
    
if __name__ == '__main__':
    unittest.main()

