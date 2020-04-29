#!/usr/bin/python
import my_pkg

def make_list(line):
    line = line.replace('[', '')
    line = line.replace(']', '')
    line = line.replace(',', ' ')
    llist = line.split()
    llist  = list(map(int, llist))

    return llist
    


if __name__=='__main__' :
    while 1:
        menu = input("Select menu: 1) conversion 2) union/intersection 3)exit ? ")

        if menu == '1' :
            binary = input("input binary number: ")
            print("=> OCT>", my_pkg.toOctal(binary))
            print("=> DEX>", my_pkg.toDecimal(binary))
            print("=> HEX>", my_pkg.toHexadecimal(binary))
        elif menu == '2' :
            fline = input("1st list: ")
            flist = make_list(fline)
            sline = input("2nd list: ")
            slist = make_list(sline)
            print("=> union", my_pkg.union(flist, slist))
            print("=> intersection", my_pkg.intersection(flist, slist))
        elif menu == '3' :
            print("exit the program...")
            exit(0)
        else :
            print("[Error] Wrong input.")
