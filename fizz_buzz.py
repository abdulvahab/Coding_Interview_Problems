#!/usr/bin/env python
'''This Script print out numbers from 1 to upperlimit(set to 100).
   Instead of nubmer which is multiple of fizz (set to 3), it will print "Fizz",
   for number which is multiple of buzz(set to 7) , output will be "Buzz",
   for number which is multiple of both fizz & buzz(set to 3 & 7) , will print "FizzBuzz"

   Created By : Abdulvahab Kharadi on 20/07/2018 '''


def fizzBuzz(fizz=3, buzz=7, upto=100, show=10):
    '''This function takes four optional argument,
    1) fizz(set to 3)
    2) buzz(set to 7)
    3) upto = upperlimit of range(of numbers) to process(by default set to 100 ),
    4) show = number of result to view for easy analysis(set to 10)
    Output: "Fizz","Buzz,"FizzBuzz" or original number as rule specified above '''

    for number in range(1, upto):
        if (number % fizz == 0) and (number % buzz == 0):
            print("FizzBuzz")              # check divisibility by fizz & buzz
        elif number % fizz == 0:
            print("Fizz")                  # check divisibility by fizz
        elif number % buzz == 0:
            print("Buzz")                  # check divisibility by buzz
        else:
            # numbers not divisible by fizz and/or buzz
            print(number)
        while (number % show == 0):        # while loop to print break meassage after each show
            input("Press Enter to See next 10 results: ")
            number += 1


if "__name__ == __main__":

    fizzBuzz()
