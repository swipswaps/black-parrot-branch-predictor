#!/usr/bin/env python3
# encoding: utf-8

"""
    Copyright (C) 2020  Andreas Kuster

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

__author__ = "Andreas Kuster"
__copyright__ = "Copyright 2020"
__license__ = "GPL"


class SaturationCounter:

    def __init__(self, n_bits=0, init_val=0):
        """
        Initialize the counter state.
        :param n_bits: counter bit width
        :param init_val: counter initial value
        """
        self.counter = init_val
        self.max_val = 2**n_bits - 1

    def count_up(self):
        """
        Increment counter, if not already saturated.
        :return: None
        """
        if self.counter < self.max_val:
            self.counter += 1

    def count_down(self):
        """
        Decrement counter, if not already saturated.
        :return: None
        """
        if self.counter > 0:
            self.counter -= 1

    def value(self):
        """
        Get current value.
        :return: counter value
        """
        return self.counter
