import unittest
import sys
import setup
import inference
from io import StringIO
from unittest.mock import patch

CODE_PATH = setup.pathlib.Path(__file__).parent.absolute()I
PACKAGE_PATH = CODE_PATH.pareInt.absolute()
DATA_PATH = str(PACKAGE_PATH) + "/data"

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
		cwd = setup.os.getcwd()
		print("Current directory:", cwd)
		print("Changing directory to package directory:", PACKAGE_PATH)
		setup.os.chdir(PACKAGE_PATH)
		print("Removing venv")
		setup.os.system("rm -rf env/")
		print("Changing directory:", cwd)
		setup.os.chdir(cwd)
		print("DONE")

	def tearDown(self):
		print("TEARING DOWN")

		# reset config files
		cmd = "git checkout -- "
		config_path = "/deepmedic/inference_model/config"
		cmd += PACKAGE_PATH + config_path

		setup.os.system(cmd + "/model/modelConfig.cfg")
		setup.os.system(cmd + "/test/testConfig.cfg")
		setup.os.system(cmd + "/test/testNamesOfPredictions.cfg")
		setup.os.system(cmd + "/test/test_flair.cfg")
		setup.os.system(cmd + "/test/test_t1w.cfg")

		# erase test data
		if setup.os.path.exists(DATA_PATH):
			print("Data found - deleting")
			setup.shutil.rmtree(DATA_PATH)
			print("Deleted")
		else:
			print("Data NOT found")

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
		path_mc = str(PACKAGE_PATH) + "/deepmedic/inference_model/config/model/modelConfig.cfg"
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

	def test_modifyTC_modifiesOutputFolder(self):
		print("ARRANGE - MODIFYTC")
		print("-"*20)
		path_tc = str(PACKAGE_PATH) + "/deepmedic/inference_model/config/test/testConfig.cfg"
		print("Path to TC:", path_tc)

		print("ACT - MODIFYTC")
		print("-"*20)
		inference.modifyTC()

		print("ASSERT - MODIFYTC")
		print("-"*20)
		old = "\"/ifs/loni/faculty/farshid/img/members/jack/dmtest/deepmedic/trial_3_pipeline/output/\""
		with open(path_tc,'r') as f:
			content = f.read()
		index1 = content.find("folderForOutput = ")
		substr = "#  [Optional] Path to a saved model, to load parameters from in the beginning of the session. If one is also specified using the command line, the latter will be used."
		index2 = content.find(substr)
		new = content[index1 + len("folderForOutput = "):index2]
		print(old)
		print(new)
		self.assertNotEqual(old, new)

	def test_modifyCfgs_modifiesPred_both(self):
		print("ARRANGE - MODIFYCFGS (MODIFIESPRED_BOTH)")
		print("-"*20)
		# make test data folder
		cwd = setup.os.getcwd()
		setup.os.chdir(

		print("ACT - MODIFYCFGS (MODIFIESPRED_BOTH)")
		print("-"*20)
		inference.modifyCfgs(DATA_PATH)

		print("ASSERT - MODIFYCFGS (MODIFIESPRED_BOTH)")
		print("-"*20)
		self.assert

	def test_modifyCfgs_modifiesPred_t1wOnly(self):
		pass

	def test_modifyCfgs_modifiesPred_flairOnly(self):
		pass

	def test_modifyCfgs_modifesT1w(self):
		pass

	def test_modifyCfgs_modifesFlair(self):
		pass

if __name__ == "__main__":
	unittest.main()
