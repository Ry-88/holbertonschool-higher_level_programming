#!/usr/bin/python3
"""
This module demonstrates extending Python's built-in list class to
add custom behavior. The VerboseList class prints notifications
whenever items are added or removed from the list.
"""

class VerboseList(list):
    """
    A custom list class that prints notifications whenever elements
    are added or removed.
    """

    def append(self, item):
        """
        Add an item to the end of the list and print a message.
        """
        super(VerboseList, self).append(item)
        print("Added {} to the list.".format(item))

    def extend(self, iterable):
        """
        Extend the list with elements from the iterable and print a message.
        """
        count = len(iterable)
        super(VerboseList, self).extend(iterable)
        print("Extended the list with {} items.".format(count))

    def remove(self, item):
        """
        Remove the first occurrence of item and print a message.
        """
        print("Removed {} from the list.".format(item))
        super(VerboseList, self).remove(item)

    def pop(self, index=-1):
        """
        Remove and return the item at the given index and print a message.
        """
        item = self[index]
        print("Popped {} from the list.".format(item))
        return super(VerboseList, self).pop(index)


if __name__ == "__main__":
    # Testing VerboseList
    vlist = VerboseList([1, 2, 3])
    vlist.append(4)
    vlist.extend([5, 6])
    vlist.remove(2)
    vlist.pop()
    vlist.pop(0)
