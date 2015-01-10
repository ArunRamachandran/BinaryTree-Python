""" Python code to get the path sum of a tree """

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
	if head == None :
		return NewNode(obj)
	else :
		if obj <= head.data : head.left = Insert(head, obj)
		else : head.right = Insert(head, obj)
	return head

def BuildTree(head) :
	head.data = 4
	x = [1,2,3,5]
	for elem in x:
		head = Insert(head,elem)
	return head

def print_list(lst) :
	for elem in lst:
		print "%d" % (elem),
	print " "

def printPathRecur(head, paths) :
	if head == None : return
	
	paths.append(head.data)

	if head.left == None and head.right == None:
		print_list(paths)

	else :
		printPathRecur(head.left, paths)
		printPathRecur(head.right, paths)

def printpaths(head,paths) :
	printPathRecur(head,paths)
		
head = Node()
head = BuildTree(head)
paths = []
l = 0
printpaths(head,paths)
