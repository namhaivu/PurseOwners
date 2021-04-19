import math


def chart():
    n = 1
    exp = 0
    x = 0
    for n in range(100):
        print(str(exp) + " exp needed for level " + str(n) + "\n")
        x = x + (n*5)
        exp = exp + x
