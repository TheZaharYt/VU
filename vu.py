from subprocess import check_output


def cmd(command: str):
    try:

        return check_output(command, shell=True).decode("cp866").replace('\r', '')
    except :
        print("--------")



