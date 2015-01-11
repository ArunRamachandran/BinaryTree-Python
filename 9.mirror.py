""" Python  code to implement a mirror fn """

class Node :
	""" Node of a tree """
	def __init__(self) :
		self.data = None
		self.left = None
		self.right= None

def NewNode(elem) :
	node = Node()
	node.data = elem
	node.left = None
	node.right= None
	return node

def Insert(head,elem) :
	if head == None:
		return NewNode(elem)
	else :
		if elem <= head.data : head.left = Insert(head.left,elem)
		else : head.right = Insert(head.right,elem)
		return head

def buildTree(head) :
	head.data = 4
	x = [2,1,3,5]
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

def mirror(head) :
	if head == None:
		return
	else :
		temp = Node()
		mirror(head.left)
		mirror(head.right)
	
		temp = head.left
		head.left = head.right
		head.right= temp

head = Node()
head = buildTree(head)
printTree(head)
mirror(head)
print "After mirror fn "
printTree(head)

