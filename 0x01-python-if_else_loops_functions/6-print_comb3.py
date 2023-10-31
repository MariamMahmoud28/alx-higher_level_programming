#!/usr/bin/python3
for i in range(10):
    for m in range(i, 10):
        if i < m:
            print("{:d}{:d}".format(i, m),
                    end=", " if i != 8 or m != 9 else "\n")

