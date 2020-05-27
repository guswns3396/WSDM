import os


# create virtual environment for python
print("CREATING VIRTUAL ENVIRONMENT")
os.system("python3 -m venv env")
print("DONE")

# activate virtual environment
print("ACTIVATING VIRTUAL ENVIRONMENT")
os.system("source env/bin/activate")
print("DONE")

# install packages
# -----------------
print("INSTALLING DEPENDENCIES")
# upgrade pip
os.system("pip install --upgrade pip")
# install dependencies
os.system("pip install -r requirements.txt") 
print("DONE")

print("DEACTIVATING VIRTUAL ENVIRONMENT")
# deactivate virtual environment
os.system("deactivate")
print("DONE")
