 We will build a sequence by repeatedly taking inventory. We take inventory each time we add 0 to the sequence. To take inventory we start by counting the number of zeros in the sequence and add the number to the end of the sequence, then we continue by counting the number of ones and add that to the sequence and so on. We stop when we reach a number that is not in the sequence and we add 0 to the sequence then start over.

The first few terms are as follows:

0 1 2 3 4 5
-----------
0
1 1 0
2 2 2 0
3 2 4 1 1 0
4 4 4 1 4 0

Print the first 1,000 terms of the inventory sequence, each on their own line. 
