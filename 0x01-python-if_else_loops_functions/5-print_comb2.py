#!/usr/bin/python3
# 5-print_comb2.py
# Muhammed Riad

for i in range(0, 10):
    for y in range(0, 10):
        if i != 9 and y != 9:
            print("{}{}".format(i, y), end=", ")
        elif i == 9 and y == 9:
            print("{}{}".format(i, y), end="\n")
