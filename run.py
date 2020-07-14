import sys
from code import setup
from code import inference

if __name__ == '__main__':
	if len(sys.argv) == 1:
		print("Not enough command line arguments")
	else:
		# setup venv
		if sys.argv[1] == '1' and len(sys.argv) == 2:
			setup.setupVenv()
			setup.addActivator()
		# install dependencies
		elif sys.argv[1] == '2' and len(sys.argv) == 2:
			setup.install()
		# run inference
		elif sys.argv[1] == '3' and len(sys.argv) == 3:
			pass
		else:
			print("Invalid command line argument(s)")
