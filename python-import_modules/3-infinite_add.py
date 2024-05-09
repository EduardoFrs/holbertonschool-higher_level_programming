#!/usr/bin/python3
import sys

if __name__ == "__main__":

    result = 0
    for arg in range(len(sys.argv)):
        result += int(sys.argv[arg])
    print("{}".format(result))