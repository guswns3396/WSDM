import os
import pathlib
import shutil

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

def addActivator():
    print("ADDING ACTIVATOR FOR VENV")
    # get path to code folder
    code_path = pathlib.Path(__file__).parent.absolute()
    print("Code directory:", code_path)
    # get path to package folder
    package_path = code_path.parent.absolute()
    print("Package directory:", package_path)
    # get path to activate_this file
    file_path = str(code_path) + "/activate_this.py"
    print("File path:", file_path)
    # get path to bin folder
    bin_path = str(package_path + "/env/bin/")
    print("env/bin directory:", bin_path)
    # add activate_this.py
    shutil.copyfile(file_path, bin_path)
    print("DONE")

def install():
    # install packages
    # -----------------
    print("INSTALLING DEPENDENCIES")
    # get cwd
    cwd = os.getcwd()
    print("Current directory:", cwd)
    # get path to package folder
    path = pathlib.Path(__file__).parent.parent.absolute()
    print("Package directory:", path)
    # change directory to package folder then install
    print("Changing directory to:", path)
    os.chdir(path)
    print("Installin pip and dependencies")
    os.system("pip install --upgrade pip")
    # install dependencies
    os.system("pip install -r requirements.txt")
    # change directory back
    print("Changing directory to:", cwd)
    os.chdir(cwd)
    print("DONE")

    return
