import unittest
import setup

class TestSetup(unittest.TestCase):
	def test_setupVenv_installsVenv(self):
		path = setup.pathlib.Path(__file__).parent.parent.absolute()
		path += "/env/bin/python3"

		setup.setupVenv()

		self.assertTrue(setup.os.path.isfile(path))
