import unittest
from unittest.mock import patch
from employee import Employee


class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """method that is run at the beginning of the tests"""
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        """method that is run at the end of the tests"""
        print("tearDownClass")

    def setUp(self):
        """The code in this function is run before every single test"""
        print("setUp")
        self.emp_1 = Employee('Estifanos', 'Abebe', 50000)
        self.emp_2 = Employee('John', 'Michael', 60000)

    def tearDown(self):
        """The code in this function is run after every single test"""
        print("tearDown\n")

    def test_email(self):
        # emp_1 = Employee('Estifanos', 'Abebe', 50000)
        # emp_2 = Employee('John', 'Michael', 60000)
        print("test_email")
        self.assertEqual(self.emp_1.email, 'Estifanos.Abebe@email.com')
        self.assertEqual(self.emp_2.email, 'John.Michael@email.com')

        self.emp_1.first = 'Mary'
        self.emp_2.first = 'Peace'

        self.assertEqual(self.emp_1.email, 'Mary.Abebe@email.com')
        self.assertEqual(self.emp_2.email, 'Peace.Michael@email.com')

    def test_fullname(self):
        # emp_1 = Employee('Estifanos', 'Abebe', 50000)
        # emp_2 = Employee('John', 'Michael', 60000)
        print("test_fullname")
        self.assertEqual(self.emp_1.fullname, 'Estifanos Abebe')
        self.assertEqual(self.emp_2.fullname, 'John Michael')

        self.emp_1.first = 'Mary'
        self.emp_2.first = 'Peace'

        self.assertEqual(self.emp_1.fullname, 'Mary Abebe')
        self.assertEqual(self.emp_2.fullname, 'Peace Michael')

    def test_apply_raise(self):
        # emp_1 = Employee('Estifanos', 'Abebe', 50000)
        # emp_2 = Employee('John', 'Michael', 60000)
        print("test_apply_raise")
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 50000*1.05)
        self.assertEqual(self.emp_2.pay, 60000*1.05)

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:

            # Testing good response
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Abebe/May')
            self.assertEqual(schedule, 'Success')

            # Testing bad response
            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Michael/June')
            self.assertEqual(schedule, 'Bad Response')


if __name__ == '__main__':
    unittest.main()
