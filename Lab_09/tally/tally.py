import numpy as np
import sys

def main():
    filename = str(sys.argv[1])
    columnNumber = int(sys.argv[2])
    file = open_file(filename)
    return sum_column(file, columnNumber)

def open_file(filename):
    try:
        return open(filename)
    except(NameError, IOError):
        print("The requested file, %s, cannot be opened..." % filename)
        exit()

def sum_column(file, column):
    dataSum = np.sum(np.loadtxt(file), axis = 0)
    return dataSum[column]

if __name__ == "__main__":
    print (main())