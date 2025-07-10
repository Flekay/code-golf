for(i=3;i++<10;)for(a=1;a<=i;b=a^i?a:1,print(' '.repeat(i-b-1),'*'.repeat(2*b-1),a++^i?'':'\n'));
