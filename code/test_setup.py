import unittest
import setup

class TestSetup(unittest.TestCase):
	def test_setupVenv_installsVenv(self):
		path = setup.pathlib.Path(__file__).parent.parent.absolute()
		setup.os.chdir(path)
		path = str(path.parent) + "/env/bin/python3"
		print(path)

		setup.setupVenv()

		self.assertTrue(setup.os.path.exists(path))

if __name__ == "__main__":
	unittest.main()
