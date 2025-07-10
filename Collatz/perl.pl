c(N,D):-N<2,C is D,writeln(C);mod(N,2)<1,c(N/2,D+1);c(N*3+1,D+1).
:-between(1,1000,G),\+c(G,0).
