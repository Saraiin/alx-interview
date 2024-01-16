<h1>0x02-minimum_operations</h1>
<h2> Task :memo: </h2>
In a text file, there is a single character H. Your text editor can execute only two operations in this file: Copy All and Paste. Given a number n, write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file.

- Prototype: def minOperations(n)<br>
- Returns an integer<br>
- If n is impossible to achieve, return 0<br>
<b>Example:</b>
n = 9

H => Copy All => Paste => HH => Paste =>HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH

Number of operations: 6
