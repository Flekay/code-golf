B=max
import sys
for A in sys.argv[1:]:A,C,F,G,D,E,H,I=map(int,A.split());print(B(0,min(A+F,D+H)-B(A,D))*B(0,min(C+G,E+I)-B(C,E)))
