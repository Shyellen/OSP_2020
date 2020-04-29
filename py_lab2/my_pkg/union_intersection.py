#!/usr/bin/python

def union(list1, list2):
    lists = list1 + list2
    lUnion = list(set(lists))
    lUnion.sort()
    return lUnion


def intersection(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    lIntersection = set1 & set2
    lIntersection = list(lIntersection)
    lIntersection.sort()
    return lIntersection

if __name__ == '__main__':
    print("this is 'union_intersection' module of 'my_pkg' package.")

