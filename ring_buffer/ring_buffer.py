# -*- coding: utf-8 -*-
"""Circular / Ring Buffer"""


class RingBuffer:
    """Ring buffer data structure."""

    def __init__(self, capacity):
        self.index = 0
        self.capacity = capacity
        self._contents = []

    def append(self, item):
        if len(self._contents) == self.capacity:
            self._contents[self.index % self.capacity] = item
        else:
            self._contents.append(item)
        self.index = (self.index + 1)

    def get(self):
        return self._contents
