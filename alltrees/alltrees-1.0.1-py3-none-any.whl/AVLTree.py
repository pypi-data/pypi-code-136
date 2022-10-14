class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def treeHeight(self):
        return self.__getHeight(self.root)

    def __getHeight(self, temp):
        if temp is None:
            return 0
        if temp.left is not None:
            left = self.__getHeight(temp.left)
        else:
            left = 0
        if temp.right is not None:
            right = self.__getHeight(temp.right)
        else:
            right = 0
        return max(left,right)+1


    def getBalanceFactor(self,node=None,var=1):
        if node is None:
            if var==1:
                node = self.root
            else:
                return 0
        else:
            return self.__getHeight(node.left) - self.__getHeight(node.right)

    def __addNodeFunc(self,val,temp):
        if temp is None:
            return Node(val)
        else:
            if val<temp.data:
                temp.left = self.__addNodeFunc(val,temp.left)
            else:
                temp.right = self.__addNodeFunc(val,temp.right)

            balancefact = self.getBalanceFactor(temp,0)
            print(temp.data,balancefact)
            if balancefact>1:
                if val<temp.left.data:
                    return self.__rightRotate(temp)
                elif val>temp.left.data:
                    temp.left = self.__leftRotate(temp.left)
                    return self.__rightRotate(temp)
            elif balancefact<-1:
                if val>temp.right.data:
                    return self.__leftRotate(temp)
                elif val<temp.right.data:
                    temp.right = self.__rightRotate(temp.right)
                    return self.__leftRotate(temp)
            return temp

    def addNode(self,val):
        self.root = self.__addNodeFunc(val, self.root)

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
            height = self.__getHeight(temp=node)
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
                node = temp
            
            elif node.left is None:
                temp = node.right
                node = None
                node = temp
            
            elif node.left is not None and node.right is not None:
                temp = self.findMin(node.right)
                node.data = temp.data
                node.right = self.__deleteNodeFunc(temp.data,node.right)
        balancefact = self.getBalanceFactor(node,0)
        # print(node.data,balancefact)
        if balancefact>1:
            if val<node.left.data:
                return self.__rightRotate(node)
            elif val>node.left.data:
                node.left = self.__leftRotate(node.left)
                return self.__rightRotate(node)
        elif balancefact<-1:
            if val>node.right.data:
                return self.__leftRotate(node)
            elif val<node.right.data:
                node.right = self.__rightRotate(node.right)
                return self.__leftRotate(node)
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

    def __leftRotate(self,node):
        if node is None:
            return None
        else:
            rightchild = node.right
            leftchild = rightchild.left

            rightchild.left = node
            node.right = leftchild
            return rightchild
    
    def __rightRotate(self,node):
        if node is None:
            return None
        else:
            leftchild = node.left
            rightchild = leftchild.right

            leftchild.right = node
            node.left = rightchild
            return leftchild
    
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

    
tr = Tree()
tr.addNode(10)
tr.addNode(20)
tr.addNode(30)
tr.addNode(40)
tr.addNode(50)
tr.addNode(25)
tr.addNodeList([60,100,55])
print("InOrder Display")
tr.inOrderDisplay()
print("PreOrder Display")
tr.preOrderDisplay()
print("PostOrder Display")
tr.postOrderDisplay()
print(tr.deleteNode(100))
tr.printtree()
print(tr.searchNode(30))
print(tr.deleteAll())
print("InOrder Display")
tr.inOrderDisplay()
print("PreOrder Display")
tr.preOrderDisplay()
print("PostOrder Display")
tr.postOrderDisplay()