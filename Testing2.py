
import unittest

def add(a,b):
    return a+b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b


class MyApp2(unittest.TestCase):

    def setUp(self):
        self.a = 15
        self.b = 25
        # print("Setup Called")

    def tearDown(self):
        self.a = 0
        self.b = 0
        # print("Teardown Called")

    def test_case_add(self):

        #Act
        c = add(self.a, self.b)
        #Assert
        self.assertEqual(self.a + self.b, c)

    def test_case_div(self):

        c = div(self.a, self.b)
        self.assertEqual(c, self.a/self.b)

    def test_case_mul(self):

        c = mul(self.a,self.b)
        self.assertEqual(c, self.a * self.b)


if __name__ == "__main__":
    unittest.main()
