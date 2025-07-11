t=lambda x:[c+" "*(i+1)+c for i,c in enumerate(t(x-1))]+[" "*2**(x-1)+c for c in t(x-1)]if x else['▲'];*map(print,t(4)[::-1]),
