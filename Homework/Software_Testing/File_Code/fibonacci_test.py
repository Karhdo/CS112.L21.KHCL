#Importing library and Add function
import unittest
import random
from fibonacci_1 import fibonacci_1
from fibonacci_2 import fibonacci_2

#Creating class unittest
class TestAdd(unittest.TestCase):
	def test_1_manual(self):
		with open("Test1.in", 'w+') as f_in:          						#Creating new file input
			with open("Test1.out", 'w+') as f_out:    						#Creating new file output
				self.assertEqual(fibonacci_1(3,2), 15)       					#Testing Add function if its work as expected
				f_in.write('3 2')                   							#Write down test case to input file
				f_out.write('{}'.format(fibonacci_1(3,2)))  					#Write down result to output file
		with open("Test2.in", 'w+') as f_in:          						#Creating new file input
			with open("Test2.out", 'w+') as f_out:    						#Creating new file output
				self.assertEqual(fibonacci_1(1,1), 2)
				f_in.write('1 1')
				f_out.write('{}'.format(fibonacci_1(1,1)))
		with open("Test3.in", 'w+') as f_in:          						#Creating new file input
			with open("Test3.out", 'w+') as f_out:    						#Creating new file output
				self.assertEqual(fibonacci_1(1000,100000), 799894155)
				f_in.write('1 1')
				f_out.write('{}'.format(fibonacci_1(1000,100000)))
           
                
	def test_2_auto(self):
		for i in range(4, 101):
			with open("Test{}.in".format(i), 'w+') as f_in:
				with open("Test{}.out".format(i), 'w+') as f_out:
					n = random.randint(1, 1000)
					k = random.randint(1, 100000)
					self.assertEqual(fibonacci_1(n, k), fibonacci_2(n, k))    	#Comparision with a true function
					f_in.write('{} {}'.format(n, k))
					f_out.write('{}'.format(fibonacci_1(n, k)))

if __name__ == "__main__":
	unittest.main()