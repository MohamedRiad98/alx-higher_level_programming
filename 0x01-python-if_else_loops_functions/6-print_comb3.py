#!/usr/bin/python3
# Muhammed Riad

for i in range(0, 9):
    for j in range(1+i, 10):
        if i != 8 and j != 10:
            print("{}{}".format(i, j), end=", ")
        elif i == 8 and j == 9:
            print("{}{}".format(i, j), end="\n")
