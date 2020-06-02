import os

def setupVenv():
    # create virtual environment for python
    print("CREATING VIRTUAL ENVIRONMENT")
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
