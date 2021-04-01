# -*- coding: utf-8 -*-

class FizzBuzz:
    def convert(self, number):
        if(number < 1 or number > 100):
            raise Exception("1<=number<=100")
        elif(number % 3 == 0 and number % 5 == 0):
            return "FizzBuzz"
        elif(number % 3 == 0):
            return "Fizz"
        elif(number % 5 == 0):
            return "Buzz"
        else:
            return str(number)
