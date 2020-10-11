# invert a binary tree

class Node:
    def __init__(self, label):
        self.label = label
        self.left = None
        self.right = None
 
def preorder(node):
    if node == None:
        return
    print(node.label)
    preorder(node.left)
    preorder(node.right)
 
def inorder(node):
    if node == None:
        return
    inorder(node.left)
    print(node.label)
    inorder(node.right)
 
def postorder(node):
    if node == None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.label)
 
root = Node('4')
root.left = Node('2')
root.right = Node('7')
root.left.left = Node('1')
root.left.right = Node('3')
root.right.left = Node('6')
root.right.right = Node('9')
print('preorder...')
preorder(root)
print()
print('inorder...')
inorder(root)
print()
print('postorder...')
postorder(root)


""" 
import collections
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def invertTree(root: TreeNode) -> TreeNode:
  queue = collections.deque()
  queue.append(root)
  
  while len(queue) != 0:
    curr = queue.popleft()
    temp = curr.left
    curr.left = curr.right
    curr.right = temp
    if curr.left != None: queue.append(curr.left)
    if curr.right != None: queue.append(curr.right)
          
  return root

# a helper to print trees
def printTree(node, level=0, char = ""):
  if node.right: printTree(node.right, level + 1, "/ ")
  print(' ' * 4 * level + char, node.val)
  if node.left: printTree(node.left, level + 1, r"\ ")
    
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

print("before")
printTree(root)

print("after")
node = invertTree(root)
printTree(node) """




