z,g,n,b=100,' of beer on the wall','no more',' bottle'
while z:z-=1;s=b+'s'*(z!=1);print(f'{z or'N'+n[1:]}{s+g}, {z or n}{s} of beer.\n{['Take one down and pass it around','Go to the store and buy some more'][z<1]}, {(z-1)%100or n}{b+'s'*(z!=2)+g}.\n')
