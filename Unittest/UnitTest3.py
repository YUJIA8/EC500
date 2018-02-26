import unittest
import twitterWYJ
import subprocess
import time
import os


class Test3(unittest.TestCase):
	
	def test_whether_save_label(self):
		num = 0
		os.system("twitterWYJ.py")
		for file in os.listdir('.'):
			if file.endswith('txt'):
				num = num + 1
		print('The amount of ".txt" file you have created is ' + str(num) + '.')
		try:
			self.assertEqual(num,1)
			print('You have passed the Test3! Congratulations!')
		except:
			try:
				self.assertGreater(num,1)
				print('You have created more than one ".txt" files! Review your code and try again!')
			except:
				print('You have not created any ".txt" file! Review your code and try again!')		


		
if __name__ == '__main__': 
		unittest.main() 