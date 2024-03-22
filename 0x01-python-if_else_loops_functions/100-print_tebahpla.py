##!/usr/bin/python3
# Program to print alphabetical in reverse order
#                           Muhamed Riad .

for i in range(ord('z'), ord('a') - 1, -1):
    if i % 2 != 0:
        i = i - 32
    print("{:s}".format(chr(i)), end='')
