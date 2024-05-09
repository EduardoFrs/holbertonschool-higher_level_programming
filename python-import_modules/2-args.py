#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argc = len(sys.argv) - 1
    print("{} {}{}".format(argc, "argument" if argc == 1 else "arguments", "." if argc < 1 else ":"))
    if argc >= 1:
        for i in range(1, len(sys.argv)):
            arg = sys.argv[i]
            print("{}: {}".format(i, arg))