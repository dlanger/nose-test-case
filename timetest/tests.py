import time
from django.test import TestCase


class SimpleTest(TestCase):
	_multiprocess_shared_ = True 
	
	def test_sleep_10(self):
		time.sleep(10)
		
	def test_sleep_5(self):
		time.sleep(5)
		
   
