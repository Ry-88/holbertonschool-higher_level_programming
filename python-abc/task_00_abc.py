#!/usr/bin/python3
"""
This module demonstrates the use of Abstract Base Classes (ABCs) in Python.
"""

from abc import ABCMeta, abstractmethod


class Animal(object):
    """
    Abstract base class for all animals.
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def sound(self):
        """
        Abstract method that must be implemented in all subclasses.
        """
        pass


class Dog(Animal):
    """
    Dog class that inherits from Animal and implements the sound method.
    """

    def sound(self):
        """
        Returns the sound a dog makes.
        """
        return "Bark"


class Cat(Animal):
    """
    Cat class that inherits from Animal and implements the sound method.
    """

    def sound(self):
        """
        Returns the sound a cat makes.
        """
        return "Meow"


if __name__ == "__main__":
    dog = Dog()
    print(dog.sound())

    cat = Cat()
    print(cat.sound())
