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

        self.assertEqual(self.new_data.ident,1)
        self.assertEqual(self.new_data.data_id,1)
        self.assertEqual(self.new_data.website,"twitter.com")
        self.assertEqual(self.new_data.weblogin,"steve99")
        self.assertEqual(self.new_data.name,"steve")



if __name__ == '__main__':
    unittest.main()



if __name__ == '__main__':
    unittest.main()

