#!/usr/bin/python3
# 5-print_comb2.py
# Muhammed Riad

for i in range(0, 100):
    if i != 99:
        print("{:02d}".format(i), end=", ")
    else:
        print("{:02d}".format(i), end="\n")
