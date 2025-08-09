#!/usr/bin/python3
"""
This module demonstrates subclassing an iterator to track how many
items have been retrieved during iteration.
"""


class CountedIterator(object):
    """
    An iterator wrapper that counts the number of items retrieved.
    """

    def __init__(self, iterable):
        """
        Initialize the CountedIterator.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        """
        Return the iterator itself.
        """
        return self

    def next(self):
        """
        Retrieve the next item from the iterator.
        """
        try:
            item = self.iterator.next()
            self.count += 1
            return item
        except StopIteration:
            raise

    def get_count(self):
        """
        Return the number of items retrieved so far.
        """
        return self.count


if __name__ == "__main__":
    # Example usage
    numbers = [1, 2, 3, 4]

    it = CountedIterator(numbers)
    print("Iterating through numbers:")

    for num in it:
        print(num)

    print("Total items iterated:", it.get_count())
