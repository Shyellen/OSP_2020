#!/usr/bin/python

def toOctal(bnum):
    bnum = '0b'+bnum
    num = int(bnum, 2)
    #onum = oct(num)
    return format(num, 'o')

def toDecimal(bnum):
    bnum = '0b'+bnum
    dnum = int(bnum, 2)
    return dnum

def toHexadecimal(bnum):
    bnum = '0b'+bnum
    num = int(bnum, 2)
    #hnum = hex(num)
    return format(num, 'X')

if __name__ == '__main__':
    print("this is 'conversion' module of 'my_pkg' package.")
