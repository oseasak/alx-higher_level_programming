#!/usr/bin/python3
for g in range(100):
    if g == 99:
        print(g)
    else:
        print("{}".format('0' + str(g) if g < 10 else g), end=", ")
