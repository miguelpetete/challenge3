# challenge3

Collatz conjecture
Consider the sequence that would result from the following rules:

if n is even
  n(i+1) = n(i) // 2
if n is odd
  n(i+1) = n(i) * 3 + 1
For example starting at  the resulting sequence would be:

The Collatz conjecture says that this sequence always reaches 1. This has not be proven mathematically but it has been tested with very large numbers and seems to hold true.

Make a program that can write the corresponding sequence given an integer  as input.
Find the number  that would create the longest sequence. What will be the sequence length? 
Same as 2 but with . How long does the program take to find the solution?
Find a way to speed up the program in order to find the solution of 3 in less than half the time it took before. Hint: storing some of the information would reduce the need to recalculate it in the future. Bonus points if you can pass an argument to the program to toggle the speeding up.

Please submit the answer in a private repository in Github. Include a readme file showing the performance of the program when is run in your computer.
