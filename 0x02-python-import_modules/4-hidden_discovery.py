#!/usr/bin/python3

if __nam__ == "__main__":
    """Print all names defined by hidden_4 module."""
    import hidden_4

    names = dir(hidden_4)
    for nam in names:
        if nam[:2] != "__":
            print(nam)
