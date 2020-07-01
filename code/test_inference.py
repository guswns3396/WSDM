import unittest
import sys
import setup

class TestSetup(unittest.TestCase):
	def test_setupVenv_installsVenv(self):
		setup.setupVenv()

		

if __name__ == "__main__":
	unittest.main()
