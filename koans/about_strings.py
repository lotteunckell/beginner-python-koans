#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

__ = False


class AboutStrings(unittest.TestCase):

    ###########################
    # Creating String Objects #
    ###########################

    # Also referred to as literals as they literally represent
    # objects of type str

    def test_create_string_with_double_quotes(self):

        string = "Hello, world."

        assert type(string) == __

    def test_plus_concatenates_strings(self):

        string = "Hello, " + "world"

        assert __ == string

    def test_plus_will_not_modify_original_strings(self):

        hi = "Hello, "
        there = "world"
        string = hi + there

        assert __ == hi
        assert __ == there
        assert __ == string

    def test_len_returns_length_of_string(self):

        hi = "hi"

        assert __ == len(hi)

    def test_strings_can_change_case(self):

        assert __ == 'guido'.capitalize()
        assert __ == 'guido'.upper()
        assert __ == 'TimBot'.lower()
        assert __ == 'guido van rossum'.title()
        assert __ == 'ToTaLlY aWeSoMe'.swapcase()

    def test_you_can_get_a_substring_from_a_string(self):

        string = "Bacon, lettuce and tomato"

        assert __ == string[7:10]

    def test_you_can_get_a_single_character_from_a_string(self):

        string = "Bacon, lettuce and tomato"

        assert __ == string[1]

    def test_list_of_strings_can_be_joined(self):

        words = ["Sausage", "Egg", "Cheese"]  # This is a python list

        assert __ == ' '.join(words)

    def test_strings_can_be_split(self):

        string = "Sausage Egg Cheese"
        words = string.split(' ')   # note ' ' signifies whitespace

        assert [__, __, __] == words
