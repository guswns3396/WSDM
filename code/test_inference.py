import unittest
import sys
import setup
import inference
from io import StringIO
from unittest.mock import patch

class TestSetup(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		print("SETTING UP CLASS")
		print("-"*20)
		setup.setupVenv()
		setup.addActivator()
		setup.activate()
		setup.install()
		print("DONE")

	@classmethod
	def tearDownClass(cls):
		print("TEARING DOWN CLASS")
		print("-"*20)
		code_path = setup.pathlib.Path(__file__).parent.absolute()
		package_path = code_path.parent.absolute()
		cwd = setup.os.getcwd()
		print("Current directory:", cwd)
		print("Changing directory to package directory:", package_path)
		setup.os.chdir(package_path)
		print("Removing venv")
		setup.os.system("rm -rf env/")
		print("Changing directory:", cwd)
		setup.os.chdir(cwd)
		print("DONE")

	def test_displayBIDS_displaysText(self):
		print("ARRANGE - DISPLAYBIDS")
		print("-"*20)
		print("ACT - DISPLAYBIDS")
		print("-"*20)
		output = ""
		with patch("sys.stdout", new=StringIO()) as fake_out:
			inference.displayBIDS()
			output = fake_out.getvalue()
		print("ASSERT - DISPLAYBIDS")
		expected = "Please make sure the data is organized in the following fashion\n"
		expected += "myDataFolder/\n" + "\tSubject1/\n" + "\t\tanat/\n"
		expected += "\t\t\tSubject1_T1W.nii.gz\n" + "\t\t\tSubject1_FLAIR.nii.gz\n"
		self.assertEqual(expected, output)

if __name__ == "__main__":
	unittest.main()
