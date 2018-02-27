import unittest
import twitterWYJ
import subprocess
import time
import os


class Test2(unittest.TestCase):
	
	def test_whether_have_mp4(self):
		num = 0
		os.system("twitterWYJ.py")
		for file in os.listdir('.'):
			if file.endswith('mp4'):
				num = num + 1
		print('The amount of ".mp4" video file you have created is ' + str(num) + '.')
		try:
			self.assertEqual(num,1)
			print('You have passed the Test2! Congratulations!')
		except:
			try:
				self.assertGreater(num,1)
				print('You have created more than one ".mpt" files! Review your code and try again!')
			except:
				print('You have not created any ".mp4" file! Review your code and try again!')


	
if __name__ == '__main__': 
		unittest.main() 