# grokking
compilation of notes from grokking's algorithms txtbook

# memory 
## objectives 
- arrays and linked lists
- first sorting algorithm 
	- most algoithms work if data is sorted such as binary search which requires sorted list. 
	- selection sort -> quicksort

## Linked lists
- items can be anywhere in memory
- better for inserts
- good if you're going to read all the items one at a time.
	- Reading o(n)
	- Insertion o(1)
	- Deletion o(1)
		- Common practice to keep track of the first and last items in a linked list so it would only take o(1) time to delete

## Arrays
- better for reading random elements.
	- Reading o(1)
	- Insertion o(n)
	- Deletion o(n)
