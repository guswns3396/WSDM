import sys
from code import setup
from code import inference

if __name__ == '__main__':
	if len(sys.argv) == 1:
		print("Not enough command line arguments")
	else:
		# setup venv & install dependencies
		if sys.argv[1] == '1' and len(sys.argv) == 2:
			setup.setupVenv()
			# setup.addActivator()
			# setup.activate()
		elif sys.argv[1] == '2' and len(sys.argv) == 2:
			setup.install()
		# run inference
		elif sys.argv[1] == '3' and len(sys.argv) == 4:
			inference.displayBIDS()

			# setup.activate()

			inference.modifyMC()
			inference.modifyTC()

			inference.modifyCfgs(inference.getAbsolutePath(sys.argv[2]))

			inference.runInf(sys.argv[3])

			inference.moveOutput()

			inference.revertCfgs()
		else:
			print("Invalid command line argument(s)")
