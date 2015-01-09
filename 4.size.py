""" Python code to get the size ( no of nodes) of a BST """

class Node :
	""" Node of a Tree """
	def __init__(self) :	
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
		if obj <= head.data: head.left = Insert(head.left, obj)
		else : head.right = Insert(head.right, obj)
		return head

def BuildTree(head) :
	head.data = 9
	lst = range(3,15,2)
	for elem in lst:
		head = Insert(head, elem)
	return head

def printTree(head) :
	if head == None :
		return
	else :
		print "Data : %d" % (head.data)

	printTree(head.left)
	printTree(head.right)

def size(head) :
	if head == None :
		return 0
	else :
		return size(head.left) + 1 + size(head.right)
head = Node()
head = BuildTree(head)
printTree(head)
x = size(head)
print "Size of the Tree : %d" % (x)
