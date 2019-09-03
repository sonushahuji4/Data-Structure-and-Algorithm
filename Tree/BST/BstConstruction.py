class Node:
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self,value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value,self.root)

    def _insert(self,value, cur_node):

        if value < cur_node.data:
            if cur_node.left == None:
                cur_node.left = Node(value)
            else:
                self._insert(value,cur_node.left)

        elif value > cur_node.data:
            if cur_node.right == None:
                cur_node.right = Node(value)
            else:
                self._insert(value,cur_node.right)

        else:
            print("Data already exits")

    def findData(self,key):

        if self.root: # if root is not None i.e if contains some data
            is_found = self._findData(key,self.root)
            if is_found:
                return True
            return False
        else:
            return None

    # Searching a data in BST
    def _findData(self,key,cur_node):

        if key < cur_node.data and cur_node.left:
            return self._findData(key,cur_node.left)

        elif key > cur_node.data and cur_node.right:
            return self._findData(key,cur_node.right)
        else:
            if key == cur_node.data:
                return True

    def preOrderTraversal(self):
        cur_node = self.root
        self._preOderTraversal(cur_node)

    def _preOderTraversal(self,cur_node):
        if cur_node is None:
            return None
        else:
            print(cur_node.data,end=" ")
            self._preOderTraversal(cur_node.left)
            self._preOderTraversal(cur_node.right)

    def inOrderTraversal(self):
        cur_node = self.root
        self._inOrderTraversal(cur_node)

    def _inOrderTraversal(self,cur_node):

        if cur_node is None:
            return None
        else:
            self._inOrderTraversal(cur_node.left)
            print(cur_node.data,end=" ")
            self._inOrderTraversal(cur_node.right)

    def postOrderTraversal(self):
        cur_node = self.root
        self._postOrderTraversal(cur_node)

    def _postOrderTraversal(self,cur_node):

        if cur_node is None:
            return None
        else:
            self._postOrderTraversal(cur_node.left)
            self._postOrderTraversal(cur_node.right)
            print(cur_node.data, end=" ")

    def deleteNode(self,value):
        cur_node = self.root
        self._deleteNode(value,cur_node)

    def _deleteNode(self,value,cur_node):
        while cur_node != None and value != cur_node.data:
            pre_node = cur_node
            if value <= cur_node.data:
                cur_node = cur_node.left
            else:
                cur_node = cur_node.right

        if cur_node != None:
            # checking whether it is a leaf Node
            if cur_node.left == None and cur_node.right == None:

                if pre_node.left.data == value:
                    pre_node.left = None
                    print(cur_node.data," is delete successfully")

                if pre_node.right.data == value:
                    pre_node.right = None
                    print(cur_node.data," is delete successfully")
            else: # checking if it is branch || parent node
                if pre_node.left.data == value:
                    if cur_node.data == value:
                        cur_node.right.left = cur_node.left
                        pre_node.left = cur_node.right
                        cur_node.left = None
                        cur_node.right = None
                        print(cur_node.data, " is delete successfully")

                if pre_node.right.data == value:
                    if cur_node.data == value:
                        cur_node.right.left = cur_node.left
                        pre_node.right = cur_node.right
                        cur_node.left = None
                        cur_node.right = None
                        print(cur_node.data, " is delete successfully")



    def searchData(self,value): # search data using pre-Order Traversal
        cur_node = self.root
        self._searchData(value,cur_node)

    def _searchData(self,value,cur_node):
        if cur_node is None:
            return None
        else:
            if cur_node.data == value:
                print(cur_node.data," is present")
            self._searchData(value,cur_node.left)
            self._searchData(value,cur_node.right)
root = BST()

data = [10,8,20,3,9,15,25]
for val in data:
    root.insert(val)

print("Pre-Order Traversal")
root.preOrderTraversal()

print()

print("In-Order Traversal")
root.inOrderTraversal()

print()

print("Post-Order Traversal")
root.postOrderTraversal()

print()
print("performing search operation")
root.searchData(300)
# print()
# root.deleteNode(20)

# root.insert(5)
#
# print(root.findData(18))