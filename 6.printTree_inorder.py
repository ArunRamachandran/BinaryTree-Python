""" To iterate oever the nodes to print them out in increasing order """

class Node :
	""" Node of a tree """
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
		if obj <= head.data : head.left = Insert(head.left, obj)
		else : head.right = Insert(head.right, obj)
	return head

def BuildTree(head) :
	head.data = 4
	x = [1,2,3,5]
	for elem in x:
		head = Insert(head,elem)
	return head

def printTree(head) :
	if head == None:
		return 
	else :
		printTree(head.left)
		print "Data : %d" % (head.data)
		printTree(head.right)

head = Node()
head = BuildTree(head)
printTree(head)
