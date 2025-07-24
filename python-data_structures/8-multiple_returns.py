#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        C = None
        L = len(sentence)
    else:
        C = sentence[0]
        L = len(sentence)
    return (L, C)
