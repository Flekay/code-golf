b=1;m=4**50
exec("print(f'{b:0100b}'.translate(' █'*25));b=b^b*2%m|b&~b//2%m;"*100)
