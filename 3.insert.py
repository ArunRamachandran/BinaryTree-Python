"""Python code to insert a new node to the right place in a BST """

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

def Insert(head, obj):
	if head == None:
		print "Created new Node with data : %d" % (obj)
		return NewNode(obj)
	else :
		if obj <= head.data : head.left = Insert(head.left, obj)
		if obj > head.data :  head.right= Insert(head.right, obj)

		return head # returning unchanged node pointer """

def print_Tree(head) :
	if head == None :
		return
	else :
		print "Data : %d" % (head.data)
	
	print_Tree(head.left)
	print_Tree(head.right)

def Build() :
	head = NewNode(5)
	return head

head = Node()
head = Build()

x = range(2,15,2)
for elem in x:
	head = Insert(head, elem)
print_Tree(head)
	

