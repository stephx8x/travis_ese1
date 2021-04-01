# -*- coding: utf-8 -*-
from unittest import TestCase
from fizzbuzz import FizzBuzz


class FizzBuzzTest(TestCase):
    def setUp(self):
        self.fizzbuzz = FizzBuzz()

    def tearDown(self):
        self.fizzbuzz = None

    def test_returns_number_for_input_not_divisible_by_3_or_5(self):
        self.assertEqual('1',  self.fizzbuzz.convert(1))
        self.assertEqual('2',  self.fizzbuzz.convert(2))
        self.assertEqual('4',  self.fizzbuzz.convert(4))
        self.assertEqual('7',  self.fizzbuzz.convert(7))
        self.assertEqual('11', self.fizzbuzz.convert(11))
        self.assertEqual('13', self.fizzbuzz.convert(13))
        self.assertEqual('14', self.fizzbuzz.convert(14))

    def test_returns_number_for_input_divisible_by_3(self):
        fizzbuzz = FizzBuzz()
        self.assertEqual('Fizz', fizzbuzz.convert(3))
        self.assertEqual('Fizz', fizzbuzz.convert(6))
        self.assertEqual('Fizz', fizzbuzz.convert(9))

    def test_returns_number_for_input_divisible_by_5(self):
        fizzbuzz = FizzBuzz()
        self.assertEqual('Buzz', fizzbuzz.convert(5))
        self.assertEqual('Buzz', fizzbuzz.convert(10))
        self.assertEqual('Buzz', fizzbuzz.convert(20))

    def test_returns_number_for_input_divisible_by_3_and_5(self):
        fizzbuzz = FizzBuzz()
        self.assertEqual('FizzBuzz', fizzbuzz.convert(15))
        self.assertEqual('FizzBuzz', fizzbuzz.convert(30))
        self.assertEqual('FizzBuzz', fizzbuzz.convert(45))

    def test_number_between_1_and_100(self):
        fizzbuzz = FizzBuzz()
        with self.assertRaises(Exception):
            fizzbuzz.convert(-1)
        with self.assertRaises(Exception):
            fizzbuzz.convert(0)
        with self.assertRaises(Exception):
            fizzbuzz.convert(101)
