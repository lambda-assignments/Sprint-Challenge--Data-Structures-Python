# -*- coding: utf-8 -*-
"""Checking for duplicate names."""
import time


class BSTNode(object):
    """Binary search tree node"""
    __slots__ = '_value', 'left', 'right'

    def __init__(self, value):
        self._value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self._value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)

    def contains(self, target):
        if target == self._value:
            return True
        elif target < self._value:
            return False if self.left is None else self.left.contains(target)
        else:
            return False if self.right is None else self.right.contains(target)


start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# duplicates = list(set(names_1).intersection(names_2))  # runtime: ~ 0.0035 seconds

duplicates = []

bst_1 = BSTNode('')
bst_2 = BSTNode('')

for x in names_1:
    bst_1.insert(x)

for x in names_2:
    bst_2.insert(x)

for x in names_1 + names_2:
    if bst_1.contains(x) and bst_2.contains(x) and x not in duplicates:
        duplicates.append(x)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
