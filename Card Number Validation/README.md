 The Luhn algorithm is a simple check digit formula used to validate a variety of identification numbers.

Given a list of 16-digit payment card numbers (like 3566 0020 2036 0505), output the ones that are valid according to the Luhn algorithm. The digits of each input are separated into groups of four by spaces.

To verify a 16-digit card number like XyXy XyXy XyXy XyXy, add up all the "y" digits and the digit sums of the doubles of the "X" digits. The card number is valid if this sum is divisible by 10. 
