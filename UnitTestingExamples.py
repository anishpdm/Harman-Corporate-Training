import sys
import unittest

def myList():
    list = [1, 2, 3, 'anish', 34]
    return list

def add(x, y):
    return x+y

def check_even_or_Odd(x):
    if x % 2 == 0:
        return "even"
    else:
        return "odd"

def check_divisbleby7(x):
    if x % 7 == 0:
        return True
    else:
        return False

def LogIn(username, password):
    if username == "admin" and password == "12345":
        return True
    else:
        return False


class MyListChecker(unittest.TestCase):
    def test_list(self):
        element = 23
        self.assertNotIn(element, myList())


class LogInCheck(unittest.TestCase):

    @unittest.skip("Skipped this test")
    def test_login_check(self):
        username = "admin"
        password = "12345"
        result = LogIn(username, password)
        self.assertTrue(result)


class CheckDivisble(unittest.TestCase):

    @unittest.skipIf(sys.platform.startswith("darwin"), "requires NOT Windows OS")
    def test_case_check_divisble_1(self):
        result = check_divisbleby7(4)
        self.assertFalse(result)

    @unittest.skipUnless(sys.platform.startswith("win"), "requires NOT Windows OS")
    def test_case_check_divisble_2(self):
        result = check_divisbleby7(14)
        self.assertTrue(result)

class MyEvenorOddApp(unittest.TestCase):

    def test_case_even_or_Odd1(self):
        result = check_even_or_Odd(2)
        self.assertEqual("even", result)

    def test_case_even_or_Odd2(self):
        result = check_even_or_Odd(5)
        self.assertNotEqual("even", result)

class MyApp2(unittest.TestCase):

    def test_case_add(self):
        a = 12
        b = 22
        c = add(a, b)
        self.assertEqual(a+b, c)

    def test_case_add1(self):
        a = 12.34
        b = 34.5
        c = add(a, b)
        self.assertEqual(c, a+b)

    def test_case_add3(self):
        a = -12
        b = -2
        c = add(a,b)
        self.assertEqual(c, a+b)


if __name__ == "__main__":
    unittest.main()
