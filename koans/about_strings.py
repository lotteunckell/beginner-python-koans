#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

__ = False


class AboutStrings(unittest.TestCase):


    def test_create_string_with_double_quotes(self):

        string = "Hello, world."

        # assert that the type of string is str:
        assert type(string) == str

    def test_create_string_out_of_an_integer(self):

        string = str(123)

        # assert that the type of string is str:
        assert type(string) == str

    def test_plus_concatenates_strings(self):

        string = "Hello, " + "world"

        assert "Hello, world" == string

    def test_plus_will_not_modify_original_strings(self):

        hi = "Hello, "
        there = "world"
        string = hi + there

        assert "Hello, " == hi
        assert "world" == there
        assert "Hello, world" == string

    def test_len_returns_length_of_string(self):

        hi = "hi"

        assert 2 == len(hi)

    def test_strings_can_be_split(self):

        string = "Sausage Egg Cheese"
        words = string.split()

        assert ["Sausage", "Egg", "Cheese"] == words

    def test_strings_can_be_joined(self):

        words = ["Now", "is", "the", "time"]

        assert "Now is the time" == ' '.join(words)

    def test_use_format_to_interpolate_variables(self):

        value1 = 'one'
        value2 = 2
        string = "The values are {0} and {1}".format(value1, value2)

        assert "The values are one and 2" == string

    def test_strings_can_change_case(self):

        assert 'Guido' == 'guido'.capitalize()
        assert 'GUIDO' == 'guido'.upper()
        assert 'timbot' == 'TimBot'.lower()
        assert 'Guido Van Rossum' == 'guido van rossum'.title()
        assert 'tOtAlLy AwEsOmE' == 'ToTaLlY aWeSoMe'.swapcase()

    def test_you_can_get_a_substring_from_a_string(self):

        string = "Bacon, lettuce and tomato"

        assert "lett" == string[7:10]

    def test_you_can_get_a_single_character_from_a_string(self):

        string = "pears, lettuce and tomato"

        assert "e" == string[1]

    def test_if_a_string_contains_another_string(self):

        string = "Pears, lettuce and tomato"
        is_lettuce_in = "lettuce" in string

        assert is_lettuce_in == True

        is_dog_in = "dog" in string

        assert is_dog_in == False
