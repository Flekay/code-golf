b=1;m=4**50
exec("print(f'{b:0100b}'.translate({48:32,49:9608}));b=b^b*2%m|b&~b//2%m;"*100)
