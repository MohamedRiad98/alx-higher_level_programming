#!/usr/bin/python3
#3-print_alphabt.py
#Muhammed Riad

for i in range(ord('a'), ord('z') + 1):
    if i == ord('q') or i == ord('e'):
        continue
    print("{:c}".format(i), end="")
