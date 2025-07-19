#!/usr/bin/python3
def fizzbuzz():
    n = 1
    while n <= 100:
        three = n % 3
        five = n % 5
        all_mod = three + five

        if n == 100:
            print("Buzz", end=" ")
            break
        elif all_mod == 0:
            print("FizzBuzz", end=' ')
        elif three == 0:
            print("Fizz", end=' ')
        elif five == 0:
            print("Buzz", end=' ')
        else:
            print(n, end=' ')
        n += 1
