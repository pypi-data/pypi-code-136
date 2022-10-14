class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def addNode(self,val):
        if self.root is None:
            self.root = Node(val)
        else:
            temp = self.root
            while temp:
                if val>=temp.data:
                    if temp.right is None:
                        temp.right = Node(val)
                        break
                    temp = temp.right
                else:
                    if temp.left is None:
                        temp.left = Node(val)
                        break
                    temp = temp.left
        # if val>=temp.data:
        #     temp.right = Node(val)
        # else:
        #     temp.left = Node(val)
    def addNodeList(self,nodelist):
        if type(nodelist)!=type(list()):
            raise Exception("Expected a list")
        if len(nodelist)<1:
            raise Exception("Received a blank list")
        else:
            for node in nodelist:
                if type(node)!=type("") and type(node)!=type(0) and type(node)!=type(1.0):
                    raise Exception("Expected a string or int or float as values in the list")
                else:
                    self.addNode(node)

    def __preOrder(self,temp=None):
        if temp is None:
            temp = self.root
            if temp is None:
                print("There are no nodes in the tree")
                return
        print(temp.data,end = " ")
        if temp.left:
            self.__preOrder(temp.left)
        if temp.right:
            self.__preOrder(temp.right)
    
    def preOrderDisplay(self):
        self.__preOrder()
        print()
        
    def __inOrder(self,temp=None):
        if temp is None:
            temp = self.root
            if temp is None:
                print("There are no nodes in the tree")
                return
        if temp.left:
            self.__inOrder(temp.left)
        print(temp.data,end=" ")
        if temp.right:
            self.__inOrder(temp.right)
    
    def inOrderDisplay(self):
        self.__inOrder()
        print()

    def __postOrder(self,temp=None):
        if temp is None:
            temp = self.root
            if temp is None:
                print("There are no nodes in the tree")
                return
        if temp.left is not None:
            self.__postOrder(temp.left)
        if temp.right is not None:
            self.__postOrder(temp.right)
        print(temp.data,end = " ")
    
    def postOrderDisplay(self):
        self.__postOrder()
        print()

    def __searchNodeFunc(self,val,temp=None):
        if temp is None:
            temp = self.root
            if temp is None:
                return temp
        if temp.data == val:
            return temp
        elif val>=temp.data:
            if temp.right:
                return self.__searchNodeFunc(val,temp.right)
            else:
                return None
        elif val<temp.data:
            if temp.left:
                return self.__searchNodeFunc(val,temp.left)
            else:
                return None
        return None
    
    def searchNode(self,val):
        node = self.__searchNodeFunc(val)
        if node is not None:
            height = self.getHeight(temp=node)
            return True, height
        else:
            return False, None

    def findMin(self,temp=None):
        if temp is None:
            temp = self.root
            if temp is None:
                return None
        while temp.left is not None:
            temp = temp.left
        return temp
    
    def findMax(self,temp=None):
        if temp is None:
            temp = self.root
            if temp is None:
                return  None
        while temp.right is not None:
            temp = temp.right
        return temp

    def getHeight(self,temp=None):
        if temp is None:
            temp = self.root
            if temp is None:
                return 0
        if temp.left:
            left = self.getHeight(temp.left)
        else:
            left = 0
        if temp.right:
            right = self.getHeight(temp.right)
        else:
            right = 0
        return max(left,right)+1

    def __deleteNodeFunc(self,val,node=None):
        if node is None:
            node = self.root
            if node is None:
                return node
        if self.root.left is None and self.root.right is None:
            val = str(input("Do you want to delete the only node left in the tree? (Y|N) "))
            if val.lower()=="y" or val.lower()=="yes":
                self.root = None
                node = None
                return node
            else:
                print("Aborting Delete...")
                return self.root
        elif val>node.data:
            node.right = self.__deleteNodeFunc(val,node.right)
        elif val<node.data:
            node.left = self.__deleteNodeFunc(val,node.left)
        elif val==node.data:
            if node.right is None:
                temp = node.left
                node = None
                return temp
            
            elif node.left is None:
                temp = node.right
                node = None
                return temp
            
            elif node.left is not None and node.right is not None:
                temp = self.findMin(node.right)
                node.data = temp.data
                node.right = self.__deleteNodeFunc(temp.data,node.right)
        return node


    def deleteNode(self,val,node=None):
        conf = self.__searchNodeFunc(val)
        if conf is not None:
            val = self.__deleteNodeFunc(val,node)
            return True
        else:
            return False
    
    def deleteAll(self):
        try:
            if self.root is not None:
                while self.root.left is not None and self.root.right is not None:
                    val = self.__deleteNodeFunc(self.root.data)
                self.root = None
            return True
        except:
            return False

    def __print(self, node, indent, last):
        if node is not None:
            print(indent,end="")
            if last:
                print("R----",end="")
                indent += "     "
            else:
                print("L----",end="")
                indent += "|    "
            print(str(node.data))
            self.__print(node.left, indent, False)
            self.__print(node.right, indent, True)

    def printtree(self):
        if self.root is None:
            print("There are no nodes in the tree")
        else:
            self.__print(self.root, "", True)

# TESTING THE LIBRARY
print("Creating the tree: 10, 4 15, 5, 3, 6, 16, 14, 1")
tr = Tree()
tr.addNode(10)
tr.addNode(4)
tr.addNode(15)
tr.addNode(5)
tr.addNode(3)
tr.addNodeList([6,16,14,1])
print("Height:",tr.getHeight())
tr.printtree()
print("Search 3")
print(tr.searchNode(3))
print("Search 20")
print(tr.searchNode(20))
print("Delete 3")
print(tr.deleteNode(3))
print("Delete 10")
print(tr.deleteNode(10))
print("Delete 6")
print(tr.deleteNode(6))
print("Delete 20")
print(tr.deleteNode(20))
print("Height:",tr.getHeight())
print("In Order Display")
tr.inOrderDisplay()
print("Pre Order Display")
tr.preOrderDisplay()
print("Post Order Display")
tr.postOrderDisplay()
print("Delete the tree")
print(tr.deleteAll())
print("Height:",tr.getHeight())
print("In Order Display")
tr.inOrderDisplay()
print("Pre Order Display")
tr.preOrderDisplay()
print("Post Order Display")
tr.postOrderDisplay()