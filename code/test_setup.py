import unittest
import os
import pathlib
import setup

class TestSetup(unittest.TestCase):
	def setUp(self):
		pass
	def tearDown(self):
		if setup.os.path.exists("env"):
			setup.os.system("rm -rf env/")
	def test_setupVenv_installsVenv(self):
		path = pathlib.Path(__file__).parent.absolute()
		path = path.parent.absolute()
		print(path)
		os.chdir(path)
		print("Current Directory: " + str(os.getcwd()))
		path = str(path) + "/env/bin/python3"
		print(path)

		setup.setupVenv()

		self.assertTrue(os.path.exists(path))

if __name__ == "__main__":
	unittest.main()
