 ROT13, short for rotate by 13 places, is a simple substitution cipher derived from the Caesar cipher. It works by replacing each letter in the English alphabet with the letter 13 positions after it, wrapping around to the beginning of the alphabet if necessary.

    For uppercase letters: A becomes N, B becomes O, ..., Z becomes M.
    For lowercase letters: a becomes n, b becomes o, ..., z becomes m.
    Non-alphabetic characters (digits, punctuation, spaces) remain unchanged.

Here's a simple table that illustrates each letter substitution with ROT13:

ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm

Each argument consists of a sequence of random printable characters from the ASCII character set.

For each argument, print the sequence with all its substitutions after applying the appropriate rotations, effectively encoding or decoding the sequence, each on their own line. 
