#! /usr/bin/python3

from distutils.command.build_scripts import first_line_re


hex_chars = [i for i in range(0, 10)]
hex_chars += ["a", "b", "c", "d", "e", "f"]

possible_byte_values = []

for first_nibble in hex_chars:
    for second_nibble in hex_chars:
        possible_byte_values.append("\\x" + str(first_nibble) + str(second_nibble))

print("".join(possible_byte_values))