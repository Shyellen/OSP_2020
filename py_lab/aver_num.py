#!/usr/bin/python

n = int(input("Please enter the number of inputs: "))

sum = 0
for i in range(n):
    num = int(input(" >> input%d: " % (i+1)))
    sum += num

print("---------------")
print("average: %f" % (sum/n))
