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

	def tearDown(self):
		print("TEARING DOWN")
		code_path = setup.pathlib.Path(__file__).parent.absolute()
		package_path = str(code_path.parent.absolute())
		cmd = "git checkout -- "
		config_path = "/deepmedic/inference_model/config"
		cmd += package_path + config_path

		setup.os.system(cmd + "/model/modelConfig.cfg")
		setup.os.system(cmd + "/test/testConfig.cfg")
		setup.os.system(cmd + "/test/testNamesOfPredictions.cfg")
		setup.os.system(cmd + "/test/test_flair.cfg")
		setup.os.system(cmd + "/test/test_t1w.cfg")

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

	def test_modifyMC_modifiesOutputFolder(self):
		print("ARRANGE - MODIFYMC")
		print("-"*20)
		package_path = setup.pathlib.Path(__file__).parent.absolute().parent.absolute()
		path_mc = str(package_path) + "/deepmedic/inference_model/config/model/modelConfig.cfg"
		print("Path to MC:", path_mc)

		print("ACT - MODIFYMC")
		print("-"*20)
		inference.modifyMC()

		print("ASSERT - MODIFYMC")
		print("-"*20)
		old = "\"/ifs/loni/faculty/farshid/img/members/jack/dmtest/deepmedic/trial_3_pipeline/output/\""
		with open(path_mc,'r') as f:
			content = f.read()
		index1 = content.find("folderForOutput = ")
		index2 = content.find("#  ================ MODEL PARAMETERS")
		new = content[index1 + len("folderForOutput = "):index2]
		print(old)
		print(new)
		self.assertNotEqual(old, new)

if __name__ == "__main__":
	unittest.main()
