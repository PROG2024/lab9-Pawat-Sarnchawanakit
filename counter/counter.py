"""A singleton counter.

   counter = Counter()  get a reference to the counter. Initial count is 0.
   counter.count        property returns the current count
   counter.increment()  add 1 to current count and also return the new value

   Requirements:
   1. in Counter, do not use any static methods except __new__.
      You may not have a __new__ depending on how you implement the singleton.
"""
from typing import Self

class Counter:
    """The singleton counter class."""
    __count: int
    g_counter: Self | None = None

    def __new__(cls):
        if Counter.g_counter is not None:
            return Counter.g_counter
        new_counter = super(Counter, cls).__new__(cls)
        new_counter.__count = 0
        Counter.g_counter = new_counter
        return new_counter

    def __str__(self):
        return f"{self.__count}"

    @property
    def count(self) -> int:
        """Returns the current count."""
        return self.__count

    def increment(self) -> int:
        """Increments the count and returns the new count."""
        self.__count += 1
        return self.__count

