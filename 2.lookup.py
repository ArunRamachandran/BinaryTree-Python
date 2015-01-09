""" Python code to implement a look up fn, to check for the target in a Tree"""

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

def Build123() :
	head = Node()
	head.data = 1
	head.left = NewNode(2)
	head.right= NewNode(3)
	return head

def print_Tree(head) :
	if head == None:
		return
	else :
		print "Data : %d" % (head.data)
	print_Tree(head.left)
	print_Tree(head.right)

def lookup(target, head) :
	if head == None:
		return False
	else :
		if head.data == target :
			return True
		else :
			if target < head.data: return lookup(target, head.left)
			if target > head.data: return lookup(target, head.right)

head = Build123()
print "Created Tree : "
print_Tree(head)
x = input("Give an element to check ?\n")
case = lookup(x, head)
if case == True:
	print "Found Target in Tree"
else :
	print "Target not found in Tree"
