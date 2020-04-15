#!/usr/bin/python

n = int(input("fibonacci number: "))

a = 0
b = 1

for i in range(1, n+1):
    if (i < 2):
        print(b, end=", ")
    else:
        c = a + b
        a = b
        b = c
        if(i == n):
            print(b)
        else:
            print(b, end=", ")

print("F%d = %d" % (n, b))

