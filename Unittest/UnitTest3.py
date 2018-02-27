import unittest
import twitterWYJ
import subprocess
import time
import os


class Test1(unittest.TestCase):

	def test_running_time(self):
		begin = time.time()
		os.system("twitterWYJ.py")
		end = time.time()
		totaltime = end - begin
		print('The running time of you program is ' + str(totaltime) + '.')
		try:
			self.assertLess(totaltime,0.0028)
			print('You have passed the Test1! Congratulations!')
		except:
			print('Your running time is too long! Improve your code and try again!')

	
if __name__ == '__main__': 
		unittest.main() 