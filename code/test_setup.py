import unittest
import setup
from subprocess import Popen, PIPE

class TestSetup(unittest.TestCase):
	def setUp(self):	
		print("SETTING UP")
	
		# print paths for verification
		file_path = setup.pathlib.Path(__file__).absolute()
		print("Absolute path to current file:", file_path)
		code_path = file_path.parent.absolute()
		print("Absolute path to directory of file:", code_path)
		package_path = code_path.parent.absolute()
		print("Absoluite path to directory containing directory of file:", package_path)
		
	def tearDown(self):
		print("TEARING DOWN")

		# get cwd
		cwd = setup.os.getcwd()
		print("Current working directory:", cwd)

		# change directory to package directory
		# package_path => dm_package/
		package_path = setup.pathlib.Path(__file__).parent.absolute().parent.absolute()
		setup.os.chdir(package_path)
		print("Changed working directory to:", setup.os.getcwd())

		# check if venv exists & remove
		if setup.os.path.exists("env"):
			print("VENV FOUND - REMOVING...")
			setup.os.system("rm -rf env/")
			print("REMOVED")
		else:
			print("VENV NOT FOUND")

		# change directory back
		setup.os.chdir(cwd)
		print("Changed working directory to:", setup.os.getcwd())

	def test_setupVenv_installsVenv(self):
		print("ARRANGE - SETUPVENV")
		print("-"*20)
		file_path = setup.pathlib.Path(__file__).absolute()
		code_path = file_path.parent.absolute()
		package_path = code_path.parent.absolute()
		venv_path = str(package_path) + "/env/bin/python3"
		print("Path to venv python:", venv_path)

		print("ACT - SETUPVENV")
		print("-"*20)
		setup.setupVenv()

		print("ASSERT - SETUPVENV")
		print("-"*20)
		self.assertTrue(setup.os.path.exists(venv_path))

	def test_addActivator_copiesFile(self):
		print("ARRANGE - ADDACTIVATOR")
		print("-"*20)
		package_path = setup.pathlib.Path(__file__).parent.absolute().parent.absolute()
		print("Path to package:", package_path)
		setup.setupVenv()

		print("ACT - ADDACTIVATOR")
		print("-"*20)
		setup.addActivator()

		print("ASSERT - ADDACTIVATOR")
		print("-"*20)
		self.assertTrue(setup.os.path.exists(str(package_path) + "/env/bin/activate_this.py"))

	def test_activate_activatesVenv(self):
		print("ARRANGE - ACTIVATE")
		print("-"*20)
		code_path = setup.pathlib.Path(__file__).parent.absolute()
		print("Path to code:", code_path)
		setup.setupVenv()
		setup.addActivator()
		process = Popen(["pip","list"], stdout=PIPE)
		pip_old = process.communicate()[0].decode("utf-8")

		print("ACT - ACTIVATE")
		print("-"*20)
		setup.activate()

		print("ASSERT - ACTIVATE")
		print("-"*20)
		process = Popen(["pip", "list"], stdout=PIPE)
		pip_new = process.communicate()[0].decode("utf-8")
		print(pip_old)
		print(pip_new)
		self.assertNotEqual(pip_old, pip_new)

	def test_install_installsDependencies(self):
		print("ARRANGE - INSTALL")
		print("-"*20)
		package_path = setup.pathlib.Path(__file__).parent.absolute().parent.absolute()
		print("Path to package:", package_path)
		setup.setupVenv()
		setup.addActivator()
		setup.activate()

		print("ACT - INSTALL")
		print("-"*20)
		setup.install()

		print("ASSERT - INSTALL")
		print("-"*20)
		pip_expected = ""
		with open(str(package_path) + "/requirements.txt") as f:
			pip_expected = f.read()
		pip_expected = pip_expected.replace("\nsetuptools==46.4.0","")
		process = Popen(["pip","freeze"], stdout=PIPE)
		pip_output = process.communicate()[0].decode("utf-8")
		print(pip_expected)
		print(pip_output)
		self.assertEqual(pip_expected, pip_output)

if __name__ == "__main__":
	unittest.main()
