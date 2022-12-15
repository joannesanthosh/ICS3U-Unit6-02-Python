#!/usr/bin/env python3

# Created by: Joanne Santhosh
# Created on: Oct 2022
# This program identifies the largest number

import random


def the_largest_number(list_of_numbers):
    largest_number = list_of_numbers[0]


    for counter in range (0, len(list_of_numbers)):
        if list_of_numbers[counter] > largest_number:
            largest_number = list_of_numbers[counter]

    return largest_number


def main():
    # this function generates 10 random numbers and finds the largest one

    random_numbers = []

    # input
    for counter in range(0, 10):
        random_number = random.randint(0,100)
        random_numbers.append(random_number)
        print("{0} ".format(counter + 1, random_number))
    largest_number = the_largest_number(random_number)
    print("")
    print("The largest number is: {0} ".format(largest_number))


if __name__ == "__main__":
    main()
