#Importing library and Add function
import unittest
import random
from fibonacci_1 import fibonacci_1
from fibonacci_2 import fibonacci_2

#Creating class unittest
class TestAdd(unittest.TestCase):
    def test_1_manual(self):
        with open("Test_in.txt", 'w+') as f_in:          						#Creating new file input
            with open("Test_out.txt", 'w+') as f_out:    						#Creating new file output
                self.assertEqual(fibonacci_1(3,2), 15)       					#Testing Add function if its work as expected
                f_in.write('\n3 2')                   							#Write down test case to input file
                f_out.write('\n{}'.format(fibonacci_1(3,2)))  					#Write down result to output file

                self.assertEqual(fibonacci_1(1,1), 2)
                f_in.write('\n1 1')
                f_out.write('\n{}'.format(fibonacci_1(1,1)))

    def test_2_auto(self):
        with open("Test_in.txt", 'a+') as f_in:
            with open("Test_out.txt", 'a+') as f_out:
                for _ in range(100):                   							#Random 100 cases
                    n = random.randint(1, 1000)
                    k = random.randint(1, 100000)
                    self.assertEqual(fibonacci_1(n, k), fibonacci_2(n, k))    	#Comparision with a true function
                    f_in.write('\n{} {}'.format(n, k))
                    f_out.write('\n{}'.format(fibonacci_1(n, k)))

if __name__ == "__main__":
    unittest.main()
    '''You can also run code in terminal. Exp: python -m unittest Add_test'''
