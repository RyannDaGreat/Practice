'''
Question from https://www.careercup.com/question?id=6335704

Given a N*N Matrix. 
All rows are sorted, and all columns are sorted. 
Find the Kth Largest element of the matrix.

My solution:

We can solve with problem with O(1) space and O(N) time, where N is the width and height of the matrix.

One possible flaw in my solution: I'm not sure we're supposed to handle the edge case where we have duplicate values.
For example: 

	If we have a 3x3 matrix of 1's, what's the 3rd largest number?

	1	1	1

	1	1	1

	1	1	1
	There are two ways of answering this:
		1. There is no 3rd largest number, because this matrix only contains one value.
		2. The 3rd largest number is 1, beacause there are 9 numbers, all of which are 1.
For my solution, I'm going to assume the second case is what we're trying to find.

Let's visualize it.

Here's a matrix where the rows and columns are all sorted:

1	4	7	11	15

2	5	8	12	19

3	6	9	16	22

10	13	14	17	24

18	21	23	26	30

Note that for every element, the elements directly to it's right and directly below it are greater than that element.
It follows that the minimum will be on the top left, and that the maximum will be on the bottom right. 
It helps to visualize it diagonally:

Row:
A					1
B				2		4
C			3		5		7
D		10		6		8		11
E	18		13		9		12		15
F		21		14		16		19
G			23		17		22
H				26		24
I					30

Note that every number in row E is greater than every number in row D, 
and  that every number in row D is greater than every number in row C,etc.
There are no guarentees about the ordering of numbers within a row, however.

Let's say K=9: we're trying to find the 9th largest number in this matrix.
We know right away that our number has to come from row 
We know right away that our number can't be in row A, becuase there is only one number in A (that number being 1).
We also know it can't be in row B, because for any number in B, there can be at most two numbers less than it (the other number in row B, combined with the number in row A).
In fact, we can deduce right away that it has to come from row D, because D contains the 6th, 7th, 8th, and 9th largest numbers in the matrix.

Row:
A					•
B				•		•
C			•		•		•
D		10		6		8		11   <-- Although they're out of order, we know our 9th largest number has to be in here.

Of course, it can't come after row d, because for every number in one of those rows, there are more than 9 numbers in the matrix less than that number.

To write my program, I first created a function called get_row_number(K), which would lead me to D.

The rest is simple. First, we use radix sort to arrange the elements in this list (from least to greatest), which takes O(N) time. 
Then, we select the 3rd element in the result, which gives us the 9th largest element (because there are 6 elements before row D, and 6+3=9).
'''
