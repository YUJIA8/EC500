import unittest
import twitterWYJ
import subprocess
import time
import os


class Test1(unittest.TestCase):

	def test_time(self):
		begin = time.time()
		subprocess.call("python twitterWYJ.py",shell = True)
		end = time.time()
		totaltime = end - begin
		self.assertLess(totaltime,10)
		print('The running time of you program is ' + str(totaltime) + '.')
		print('You have passed the Test1! Congratulations!')

	
if __name__ == '__main__': 
		unittest.main() 