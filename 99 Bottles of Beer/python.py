z,g,n,b=99,' of beer on the wall','no more',' bottle'
while~z:s=b+'s'[:z^1];print(f'{z or'N'+n[1:]}{s+g}, {z or n}{s+g[:8]}.\n{z and'Take one down and pass it around'or'Go to the store and buy some more'}, {~-z%100or n}{b+'s'[:z^2]+g}.\n');z-=1
