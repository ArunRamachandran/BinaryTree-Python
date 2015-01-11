""" Python code to implement a hasPath sum fn """
""" Strategy : Substract the node value from the sum when recurring down,
and check to see if the sum is 0 when we run out of tree. """

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

def Insert(head,obj) :
	if head == None :
		return NewNode(obj)
	else :
		if obj <= head.data : head.left = Insert(head.left,obj)
		else : head.right = Insert(head.right,obj)
	return head

def buildTree(head) :
	head.data = 4
	x = [1,2,3,5]
	for elem in x:
		head = Insert(head,elem)
	return head

def hasPathSum(head,tot) :
	# Return True if we run out of tree and sum == 0
	if head == None:
		return tot == 0
	else :
		# otherwise check both subtrees
		tot = tot - head.data
		return hasPathSum(head.left,tot) or hasPathSum(head.right,tot)

head = Node()
head = buildTree(head)
path_sum = input("Give a sum to check ?")
status = hasPathSum(head,path_sum)
if status == True:
	print "Yep.. a branch has given sum"
else :
	print "Nope... It's not present"
