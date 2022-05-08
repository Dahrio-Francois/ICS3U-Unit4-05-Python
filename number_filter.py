#!/usr/bin/env python3

# Created by: Andrew-Ten-Den
# Created on: April 2022
# This program adds all positive integers


def main():
    # this function adds all positive integers

    counter = 1
    total_sum = 0
    integer = 0
    # input
    try:
        amount = int(input("Enter how many numbers you will input (ex: 10): "))
        print("")
        # process & output
        while amount >= counter:
            integer = input("Enter an integer: ")
            try:
                integer_int = int(integer)
                counter = counter + 1

                if integer_int > 0:
                    total_sum = total_sum + integer_int

                elif integer_int < 0:
                    continue

            except Exception:
                print("\nThis was not an integer\n")

        print("\nThe total sum is {}".format(total_sum))
    except Exception:
        print("\nThis was not an integer")

    print("\nDone")


if __name__ == "__main__":
    main()
