import unittest
import os
import pathlib
import setup

class TestSetup(unittest.TestCase):
	def setUp(self):	
		print("SETTING UP")
	
		# print paths for verification
		file_path = pathlib.Path(__file__).absolute()
		print("Absolute path to current file:", file_path)
		code_path = file_path.parent.absolute()
		print("Absolute path to directory of file:", code_path)
		package_path = code_path.parent.absolute()
		print("Absoluite path to directory containing directory of file:", package_path)
		
	def tearDown(self):
		print("TEARING DOWN")

		# get cwd
		cwd = os.getcwd()
		print("Current working directory:", cwd)

		# change directory to package directory
		# package_path => dm_package/
		package_path = pathlib.Path(__file__).parent.absolute().parent.absolute()
		os.chdir(package_path)
		print("Changed working directory to:", os.getcwd())

		# check if venv exists & remove
		if os.path.exists("env"):
			print("VENV FOUND - REMOVING...")
			os.system("rm -rf env/")
			print("REMOVED")
		else:
			print("VENV NOT FOUND")

		# change directory back
		os.chdir(cwd)
		print("Changed working directory to:", os.getcwd())

	def test_setupVenv_installsVenv(self):
		file_path = pathlib.Path(__file__).absolute()
		code_path = file_path.parent.absolute()
		package_path = code_path.parent.absolute()
		venv_path = str(package_path) + "/env/bin/python3"
		print("Path to venv python:", venv_path)

		print("INSTALLING VENV")
		print("-"*20)
		setup.setupVenv()
		print("-"*20)

		self.assertTrue(os.path.exists(venv_path))
'''
	def test_addActivator_copiesFile(self):
		setup.setupVenv()

		setup.addActivator()

		self.assertTrue(os.path.exists(

	def test_install_installsDependencies(self):
		# setup & activate venv
		print("SETTING UP TO INSTALL DEPENDENCIES")
		setup.setupVenv()
		

		print("INSTALLING DEPENDENCIES")
		print("-"*20)
		setup.install()
		print("-"*20)
'''
		

if __name__ == "__main__":
	unittest.main()
