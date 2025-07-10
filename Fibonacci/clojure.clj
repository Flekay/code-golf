(loop[a 1 b 0](prn b)(if(> 1e6 a)(recur(+ a b)a)a))
