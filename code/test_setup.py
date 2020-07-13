import unittest
import os
import pathlib
import setup

class TestSetup(unittest.TestCase):
	def setUp(self):
		pass
	def tearDown(self):
		# path to package directory
		print("TEARING DOWN")
		# get cwd
		cwd = os.getcwd()
		print("Current working directory:", cwd)
		# package_path => dm_package/
		package_path = pathlib.Path(__file__).parent.absolute().parent.absolute()
		os.chdir(package_path)
		print("Changed working directory to:", os.getcwd())
		if os.path.exists("env"):
			print("VENV FOUND - REMOVING...")
			os.system("rm -rf env/")
			print("REMOVED")
		else:
			print("VENV NOT FOUND")
		os.chdir(cwd)
		print("Changed working directory to:", os.getcwd())
	def test_setupVenv_installsVenv(self):
		print("SETTING UP TO INSTALL VENV")
		path = pathlib.Path(__file__).absolute()
		print("Absolute path to current file:", path)
		path = pathlib.Path(__file__).parent.absolute()
		print("Absolute path to directory of file:", path)
		path = path.parent.absolute()
		print("Absolute path to directory containing directory of file:", path)
		path = str(path) + "/env/bin/python3"
		print("Path to venv python:", path)

		print("INSTALLING VENV")
		print("-"*20)
		setup.setupVenv()
		print("-"*20)

		self.assertTrue(os.path.exists(path))
	def test_install_installsDependencies(self):
		pass

if __name__ == "__main__":
	unittest.main()
