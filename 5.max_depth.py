""" Python code to implement a max_depth fn to get the no of nodes in the largest node """

class Node:
	""" Node of a tree """
	def __init__(self):
		self.data = None
		self.left = None
		self.right= None

def NewNode(obj) :
	new = Node()
	new.data = obj
	new.left = None
	new.right= None
	return new

def Insert(head, obj) :
	if head == None:
		return NewNode(obj)
	else :
		if obj <= head.data : head.left = Insert(head.left,obj)
		else : head.right = Insert(head.right, obj)

	return head 

def BuildTree(head) :
	head.data = 6
	x = range(3,15,2)
	for elem in x:
		head = Insert(head,elem)
	return head

def printTree(head) :
	if head == None :
		return
	else :
		print "Data : %d" % (head.data)
	printTree(head.left)
	printTree(head.right)

def size(head) :
	if head == None:
		return 0
	else :
		return size(head.left) + 1 + size(head.right)

def max_depth(head):
	left_size  = size(head.left)
	right_size = size(head.right)

	if left_size > right_size:
		return left_size
	else:
		return right_size


head = Node()
head = BuildTree(head)
printTree(head)
x = max_depth(head)
print "Max Depth : %d" % (x)
