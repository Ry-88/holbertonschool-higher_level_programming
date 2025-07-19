#!/usr/bin/python3
for i in range(26):
    ch = chr(122 - i)
    print("{}".format(ch.lower() if i % 2 == 0 else ch.upper()), end='')
