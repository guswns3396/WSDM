import os


# create virtual environment for python
os.system("python3 -m venv env")

# activate virtual environment
os.system("source env/bin/activate")

# install packages
# -----------------
# upgrade pip
os.system("pip install --upgrade pip")
# install dependencies
os.system("pip install -r requirements.txt") 

# deactivate virtual environment
os.system("deactivate")
