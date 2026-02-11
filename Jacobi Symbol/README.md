 For each argument a n, print the value of the Jacobi symbol J(a, n).

Both inputs are non-negative integers, and n is odd.
J(a, 1) is defined as 1.
If n is prime, then J(a, n) is defined as 0 if a=0 (mod n), as 1 if a is a square modulo n, and −1 otherwise.
If n = x*y, x,y>1, then J(a, n) is defined as J(a, x)*J(a, y).
Note that calculating the symbol from the definition is not very efficient as it requires factorisation of n. 
