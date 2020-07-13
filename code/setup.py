import os
import pathlib

def setupVenv():
    # create virtual environment for python
    print("CREATING VIRTUAL ENVIRONMENT")
    # get cwd
    cwd = os.getcwd()
    print("Current directory:", cwd)
    # get path to package folder
    path = pathlib.Path(__file__).parent.parent.absolute()
    print("Package directory:", path)
    # change directory to package folder then install
    print("Changing directory to:", path)
    os.chdir(path)
    print("Creating virtual environment in the following directory:", path)
    os.system("python3 -m venv env")
    # change directory back
    print("Changing directory to:", cwd)
    os.chdir(cwd)
    print("DONE")
#    msg = "\nPlease activate the virtual environment by running "
#    msg += "'source env/bin/activate'"
#    msg += " before continuing with installation"
#    print(msg)

    return

def install():
    # install packages
    # -----------------
    print("INSTALLING DEPENDENCIES")
    # get path to package folder
    path = pathlib.Path(__file__).parent.parent.absolute()
    # change directory to package folder then install
    os.chdir(path)
    os.system("pip install --upgrade pip")
    # install dependencies
    os.system("pip install -r requirements.txt")
    print("DONE")

    return
