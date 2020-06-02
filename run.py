import code

def main():
    msg = "Please select from the following options:"
    msg += "\n1) Setup Virtual Environment"
    msg += "\n2) Install Dependencies"
    msg += "\n3) Run Inference"
    msg += "\n>"

    userinput = input(msg)

    if userinput == "1":
        code.setup.setupVenv()
    elif userinput == "2":
        code.setup.install()
    elif userinput == "3":
        pass
    else:
        "Invalid option"

main()
