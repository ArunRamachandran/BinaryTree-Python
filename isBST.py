""" isBST returns True if given tree is a BST , else return Flase """

class Node :
	""" Node of a tree """
	def __init__(self) :
		self.data = None
		self.left = None
		self.right= None


def Build(head) :
	head.data = 2
	new_left = Node()
	new_right= Node()
	new_left.data = 1
	new_right.data= 3
	
	head.left = new_left
	head.right= new_right

	return head

def printTree(head) :
	if head == None :
		return
	else :
		print "Data : %d" % (head.data)
		printTree(head.left)
		printTree(head.right)

def minValue(head) :
	while head.left != None :
		head = head.left
	return head.data

def maxValue(head) :
	while head.right != None :
		head = head.right
	return head.data

def isBST(head) :
	if head == None :
		return True
	if head.left != None and minValue(head.left) > head.data :
		return False
	if head.right != None and maxValue(head.right) <= head.data :
		return False
	if not isBST(head.left) or not isBST(head.right) :
		return False
	return True

head = Node()
head = Build(head)
print "Given Tree "
printTree(head)
print "Min value in the Tree "
print minValue(head)
print "Max value in the Tree "
print maxValue(head)
print isBST(head)
