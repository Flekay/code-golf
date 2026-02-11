 Given a string, output the hexdump of the string as given by the xxd utility using the default settings, as described below.

Divide up the input string into groups of 16 bytes (16 octets). For each group, print in order:

    The (hexadecimal, lowercase) index of the starting octet, padded with zeros to eight hexadecimal digits
    A single colon (:), followed by a single space.
    8 space-separated pairs of octets, with each pair printed as 4 hexadecimal digits
    Spaces to pad to 51 bytes
    The original 16 bytes, except with newline replaced with full stop (.) 
