# sample python code

class Node:
	"""Sample Tree Node """
	pass
	def __init__(self) :
		self.data = 'a'
		self.left = None
		self.right= None

def print_Tree(node) :
	print "Data : %c" % (node.data)
	if node.left == None and node.right == None:
		print "Empty Left & Right nodes"


a = Node()
print_Tree(a)


