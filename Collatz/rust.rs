fn main(){for i in 1..1001{let(mut j,mut n)=(i,0);while j>1{n+=1;j=if j%2>0{j*3+1}else{j/2}}print!("{n}
")}}
