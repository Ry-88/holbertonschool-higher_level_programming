#!/usr/bin/python3
print(", ".join(
    "{:02}".format(i) for i in range(0, 100)
), end='\n')
