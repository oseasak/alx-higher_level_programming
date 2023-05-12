#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    coun = len(sys.argv) - 1
    if coun == 0:
        print("0 arguments.")
    elif coun == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(coun))
    for f in range(coun):
        print("{}: {}".format(f + 1, sys.argv[f + 1]))
