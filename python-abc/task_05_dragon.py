#!/usr/bin/python3
"""
Module: dragon_mixins
Demonstrates the use of mixins in Python to add modular functionality
to classes without deep inheritance hierarchies.
"""


class SwimMixin:
    """
    Mixin class that provides swimming capability.
    """

    def swim(self):
        """
        Print a message indicating that the creature can swim.
        """
        print("The creature swims!")


class FlyMixin:
    """
    Mixin class that provides flying capability.
    """

    def fly(self):
        """
        Print a message indicating that the creature can fly.
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Dragon class that inherits swimming and flying capabilities
    from SwimMixin and FlyMixin.
    """

    def roar(self):
        """
        Print a message indicating that the dragon is roaring.
        """
        print("The dragon roars!")


if __name__ == "__main__":
    draco = Dragon()
    draco.swim()
