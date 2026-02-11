 The Mandelbrot set is the set of complex numbers c for which the sequence a(1) = 0, a(n+1) = a(n)² + c does not diverge to infinity.

Consider the section of the complex plane where -2 ≤ Re c ≤ 0.5, -1 ≤ Im c ≤ 1 divided into a 41×81 lattice. Draw the Mandelbrot set using this grid. That is, for each such lattice point, print █ (U+2588) if it belongs to the set and ▒ (U+2592) if it doesn't. Note that for each of the lattice points, 1063 iterations are enough to determine whether the sequence corresponding to the point is unbounded or not. 
