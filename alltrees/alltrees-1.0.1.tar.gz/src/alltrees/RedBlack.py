
# Node creation
class Node():
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1


class RedBlackTree():
    def __init__(self):
        self.NULL = Node(None)
        self.NULL.color = 0
        self.NULL.left = None
        self.NULL.right = None
        self.root = self.NULL

    # Preorder
    def pre_order(self, node):
        if node != self.NULL:
            print(node.data)
            self.pre_order(node.left)
            self.pre_order(node.right)

    # Inorder
    def in_order(self, node):
        if node != self.NULL:
            self.in_order(node.left)
            print(node.data)
            self.in_order(node.right)

    # Postorder
    def post_order(self, node):
        if node != self.NULL:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.data)

    # Search the tree

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

    # Balancing the tree after deletion
    def __fix_delete(self, x):
        while x != self.root and x.color == 0:
            if x == x.parent.left:
                s = x.parent.right
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.left_rotate(x.parent)
                    s = x.parent.right

                if s.left.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.right.color == 0:
                        s.left.color = 0
                        s.color = 1
                        self.right_rotate(s)
                        s = x.parent.right

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.right.color = 0
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.right_rotate(x.parent)
                    s = x.parent.left

                if s.right.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.left.color == 0:
                        s.right.color = 0
                        s.color = 1
                        self.left_rotate(s)
                        s = x.parent.left

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.left.color = 0
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = 0

    def __rb_transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    # Node deletion
    def delete_node(self, node, key):
        z = self.NULL
        while node != self.NULL:
            if node.data == key:
                z = node

            if node.data <= key:
                node = node.right
            else:
                node = node.left

        if z == self.NULL:
            print("Cannot find key in the tree")
            return

        y = z
        y_original_color = y.color
        if z.left == self.NULL:
            x = z.right
            self.__rb_transplant(z, z.right)
        elif (z.right == self.NULL):
            x = z.left
            self.__rb_transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.__rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.__rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 0:
            self.__fix_delete(x)

    def deleteAll(self):
        try:
            if self.root != self.NULL:
                while self.root.left is not None and self.root.right is not None:
                    self.deleteNode(self.root.data)
                self.root = self.NULL
            return True
        except:
            return False

    # Balance the tree after insertion
    def fix_insert(self, k):
        while k.parent.color == 1:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right

                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 0

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

    # Printing the tree
    def __print(self, node, indent, last):
        if node != self.NULL:
            print(indent,end="")
            if last:
                print("R----",end="")
                indent += "     "
            else:
                print("L----",end="")
                indent += "|    "

            s_color = "RED" if node.color == 1 else "BLACK"
            print(str(node.data) + "(" + s_color + ")")
            self.__print(node.left, indent, False)
            self.__print(node.right, indent, True)

    def preOrderDisplay(self):
        if self.root == self.NULL:
            print("There are no nodes to display")
        else:
            self.pre_order(self.root)

    def inOrderDisplay(self):
        if self.root == self.NULL:
            print("There are no nodes to display")
        else:
            self.in_order(self.root)

    def postOrderDisplay(self):
        if self.root == self.NULL:
            print("There are no nodes to display")
        else:
            self.post_order(self.root)

    def searchNode(self,val):
        node = self.__searchNodeFunc(val)
        print(node.data)
        if node is not None:
            height = self.getHeight(temp=node)
            return True, height
        else:
            return False, None

    def minimum(self, node):
        while node.left != self.NULL:
            node = node.left
        return node

    def maximum(self, node):
        while node.right != self.NULL:
            node = node.right
        return node

    def successor(self, x):
        if x.right != self.NULL:
            return self.minimum(x.right)

        y = x.parent
        while y != self.NULL and x == y.right:
            x = y
            y = y.parent
        return y

    def predecessor(self,  x):
        if (x.left != self.NULL):
            return self.maximum(x.left)

        y = x.parent
        while y != self.NULL and x == y.left:
            x = y
            y = y.parent

        return y

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NULL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def addNode(self, key):
        node = Node(key)
        node.parent = None
        node.data = key
        node.left = self.NULL
        node.right = self.NULL
        node.color = 1

        y = None
        x = self.root

        while x != self.NULL:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y == None:
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node

        if node.parent == None:
            node.color = 0
            return

        if node.parent.parent == None:
            return

        self.fix_insert(node)

    def getHeight(self, temp=None):
        if temp is None:
            temp = self.root
            if temp == self.NULL:
                return 0
        if temp.left != self.NULL:
            left = self.getHeight(temp.left)
        else:
            left = 0
        if temp.right != self.NULL:
            right = self.getHeight(temp.right)
        else:
            right = 0

        return (max(left,right)+1)


    def getBalanceFactor(self,node=None,var=1):
        if node is None:
            if var==1:
                node = self.root
            else:
                return 0
        else:
            return self.getHeight(node.left) - self.getHeight(node.right)

    def get_root(self):
        return self.root

    def deleteNode(self, data):
        self.delete_node(self.root, data)

    def printtree(self):
        self.__print(self.root, "", True)

if __name__ == "__main__":
    rbtree = RedBlackTree()
    rbtree.addNode("amay")
    rbtree.addNode("Madh")
    rbtree.addNode("Sam")
    rbtree.addNode("Shan")
    # rbtree.addNode(75)
    # rbtree.addNode(57)
    # rbtree.addNodeList([80,100,90])
    rbtree.printtree()
    print(rbtree.searchNode("Amay"))
    rbtree.inOrderDisplay()
    print(rbtree.getHeight())
    print("\nAfter deleting an element")
    rbtree.deleteNode("Shantanu")
    rbtree.printtree()
    rbtree.deleteAll()
    rbtree.printtree()
    # print(rbtree.getBalanceFactor(65))
    print(rbtree.getHeight())