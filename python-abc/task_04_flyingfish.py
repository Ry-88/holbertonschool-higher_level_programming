#!/usr/bin/python3
"""
This module demonstrates multiple inheritance in Python using
a FlyingFish class that inherits from both Fish and Bird.
"""


class Fish:
    """
    Represents a fish with swimming behavior and water habitat.
    """

    def swim(self):
        """Prints swimming behavior."""
        print("The fish is swimming")

    def habitat(self):
        """Prints fish habitat information."""
        print("The fish lives in water")


class Bird:
    """
    Represents a bird with flying behavior and sky habitat.
    """

    def fly(self):
        """Prints flying behavior"""
        print("The bird is flying")

    def habitat(self):
        """Prints bird habitat information"""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Represents a flying fish that can both swim and fly.
    """

    def fly(self):
        """Overrides Bird.fly()"""
        print("The flying fish is soaring!")

    def swim(self):
        """Overrides Fish.swim()"""
        print("The flying fish is swimming!")

    def habitat(self):
        """Overrides both Fish.habitat() and Bird.habitat()"""
        print("The flying fish lives both in water and the sky!")


if __name__ == "__main__":
    f_fish = FlyingFish()
    f_fish.fly()       # Overridden method
    f_fish.swim()      # Overridden method
    f_fish.habitat()   # Overridden method

    # Display method resolution order
    print("\nMethod Resolution Order:")
    print(FlyingFish.mro())
