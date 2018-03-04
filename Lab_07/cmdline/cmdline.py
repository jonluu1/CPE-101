import sys

def get_cmd_args():
    arguments_list = sys.argv
    index = 0
    for arguments in arguments_list:
        if index != 0:
            print (str(index - 1) + ": " + arguments)
        index += 1

get_cmd_args()