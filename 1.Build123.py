""" Python code to implement a Build123() Fn. """

class Node :
	""" Node of a tree """
	def __init__(self) :
		self.data = None
		self.left = None
		self.right= None 

def NewNode(bit) :
	new = Node()	
	new.data = str(bit)
	new.left = None
	new.right= None
	return new

def Build123(head) :
	head.data = '2'
	head.left = NewNode(1)
	head.right= NewNode(3)
	return head

def print_Tree(head) :
	if head == None :
		return
	else :
		print "Data : %c" % (head.data)
	print_Tree(head.left)
	print_Tree(head.right)
	
head = Node()
head = Build123(head)
print_Tree(head)

