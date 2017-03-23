# -*- coding: UTF-8 -*-
"""Week 3.

Modify each function until the tests pass.
"""
from __future__ import division
from __future__ import print_function


def loop_ranger(start, stop=None, step=1):
    """Return a list of numbers between start and stop in steps of step.

    Do this using any method apart from just using range()
    """
    step_of_step = []
    a = start

    while a != stop:
        step_of_step.append(a)
        a = a + step
    return step_of_step


def lone_ranger(start, stop, step):
    """Duplicate the functionality of range.

    Look up the docs for range() and wrap it in a 1:1 way
    """
    return range(start, stop, step)


def two_step_ranger(start, stop):
    """Make a range that steps by 2.

    Sometimes you want to hide complexity.
    Make a range function that always has a step size of 2
    """
    list = []
    i = start

    while i != stop:
        list.append(i)
        i = i+2
    return list


def gene_krupa_range(start, stop, even_step, odd_step):
    """Make a range that has two step sizes.

    make a list that instead of having evenly spaced steps
    has odd steps be one size and even steps be another.
    """
    list = []
    x = start
    step = 0

    while x <= stop:
        list.append(x)
        if step % 2 == 1:
            x = x + odd_step
        else:
            x = x + even_step
        step = step + 1
    return list


def stubborn_asker(low, high):
    """Ask for a number between low and high until actually given one.

    Ask for a number, and if the response is outside the bounds keep asking
    until you get a number that you think is OK
    """
    message = "Give me a number betwewen {low}, and {high}:".format(low=low,
                                                                    high=high)
    while True:
        input_number = int(raw_input(message))
        if low < input_number < high:
            print("{} is right.".format(input_number))
            return input_number
        else:
            print("Sorry, {input} is out of range".format(input=input_number))


def not_number_rejector(message):
    """Ask for a number repeatedly until actually given one.

    Ask for a number, and if the response is actually NOT a number (e.g. "cow",
    "six", "8!") then throw it out and ask for an actual number.
    When you do get a number, return it.
    """
    message = "Give me number:"

    while True:
        try:
            input_number = int(raw_input(message))
            print ("{} a number indeed".format(input_number))
            return(input_number)
        except Exception as e:
            print ("{} is a bad number and will be thrown out".format(e))

    return(input_number)


def super_asker(low, high):
    """Robust asking function.

    Combine stubborn_asker and not_number_rejector to make a function
    that does it all!
    """
    message = "Give me a number between {low}, and {high}:".format(low=low,
                                                                   high=high)
    while True:
        try:
            input_number = int(raw_input(message))
            if low < input_number < high:
                print("{}is right.".formwat(input_number))
            else:
                print("Sorry, {input} is out of range".format(input=input_number))
        except Exception as e:
                print ("try,again, that's not a number ({})".format(e))
        return input_number


if __name__ == "__main__":
    # this section does a quick test on your results and prints them nicely.
    # It's NOT the official tests, they are in tests.py as usual.
    # Add to these tests, give them arguments etc. to make sure that your
    # code is robust to the situations that you'll see in action.
    # NOTE: because some of these take user input you can't run them from
    # inside Atom, you need to run them from the terminal. E.g.:
    # ben@um:~/projects/git/code1161base$ python week3/exercise1.py

    print("\nloop_ranger", loop_ranger(1, 10, 2))
    print("\nlone_ranger", lone_ranger(1, 10, 3))
    print("\ntwo_step_ranger", two_step_ranger(1, 10))
    print("\ngene_krupa_range", gene_krupa_range(1, 20, 2, 5))
    print("\nstubborn_asker")
    stubborn_asker(30, 45)
    print("\nnot_number_rejector")
    not_number_rejector()
    print("\nsuper_asker")
    super_asker(33, 42)
