import os
import pahtlib

def setupVenv():
    # create virtual environment for python
    print("CREATING VIRTUAL ENVIRONMENT")
    # get path to package folder
    path = pathlib.Path(__file__).parent.parent.absolute()
    # change directory to package folder then install
    os.chdir(path)
    os.system("python3 -m venv env")
    print("DONE")
    msg = "\nPlease activate the virtual environment by running "
    msg += "'source env/bin/activate'"
    msg += " before continuing with installation"
    print(msg)

    return

def install():
    # install packages
    # -----------------
    print("INSTALLING DEPENDENCIES")
    # upgrade pip
    os.system("pip install --upgrade pip")
    # install dependencies
    os.system("pip install -r requirements.txt")
    print("DONE")

    return
