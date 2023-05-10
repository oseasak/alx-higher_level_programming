#!/usr/bin/python3
for f in range(100):
    if int(f / 10) != f % 10 and int(f / 10) < f % 10:
        print("{}{}".format(int(f / 10), f % 10), end="")
        if (f != 89):
            print(", ", end="")
print("")
