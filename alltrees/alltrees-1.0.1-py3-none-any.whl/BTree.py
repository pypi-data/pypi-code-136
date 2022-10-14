
class Node:
    def __init__(self,leaf=False):
        self.leaf = leaf
        self.keys = []
        self.children = []
    
class BTree:
    def __init__(self,order):
        self.root = Node(True)
        self.order = order
    
    def addNode(self,key):
        root = self.root
        order = self.order
        if len(root.keys)==2*order-1:
            temp = Node()
            self.root = temp
            temp.children.insert(0,root)
            self.split_child(temp,0)
            self.insert_nf(temp,key)
        else:
            self.insert_nf(root,key)
    
    def split_child(self,node,ind):
        main_node = node.children[ind]
        split_node = Node(leaf = main_node.leaf)
        order = self.order
        node.children.insert(ind+1,split_node)
        node.keys.insert(ind,main_node.keys[order-1])
        split_node.keys = main_node.keys[order:(2*order)-1]
        main_node.keys = main_node.keys[:order-1]
        if not main_node.leaf:
            split_node.children = main_node.children[order:2*order]
            main_node.children = main_node.children[:order-1]
    
    def insert_nf(self,node,key):
        i = len(node.keys)-1
        if node.leaf:
            node.keys.append(None)
            while i>=0 and key < node.keys[i]:
                node.keys[i+1] = node.keys[i]
                i-=1
            node.keys[i+1] = key
        
        else:
            while i>=0 and key < node.keys[i]:
                i-=1
            i+=1
            if len(node.children[i].keys)==2*self.order-1:
                self.split_child(node,i)
                if key>node.keys[i]:
                    i+=1
            self.insert_nf(node.children[i],key)
    
    def searchNode(self, key, node=None):
        if node is not None:
            i = 0
            while i < len(node.keys) and key > node.keys[i]:
                i += 1
            if i < len(node.keys) and key == node.keys[i]:
                return (node, i)
            elif node.leaf:
                return None
            else:
                return self.searchNode(key, node.children[i])
        else:
            return self.searchNode(key, self.root)

    def __print(self,node,level):
        print(end=" ")
        for i in node.keys:
            print(i, end=" ")
        level += 1
        if len(node.children) > 0:
            print()
            for i in node.children:
                self.__print(i, level)

    def printtree(self):
        self.__print(self.root,0)
    

    def deleteNode(self, node, key):
        t = self.t
        i = 0
        while i < len(node.keys) and k[0] > node.keys[i][0]:
            i += 1
        if node.leaf:
            if i < len(node.keys) and node.keys[i][0] == k[0]:
                node.keys.pop(i)
                return
            return

        if i < len(node.keys) and node.keys[i][0] == k[0]:
            return self.delete_internal_node(node, k, i)
        elif len(node.children[i].keys) >= t:
            self.delete(node.children[i], k)
        else:
            if i != 0 and i + 2 < len(node.children):
                if len(node.children[i - 1].keys) >= t:
                    self.delete_sibling(node, i, i - 1)
                elif len(node.children[i + 1].keys) >= t:
                    self.delete_sibling(node, i, i + 1)
                else:
                    self.delete_merge(node, i, i + 1)
            elif i == 0:
                if len(node.children[i + 1].keys) >= t:
                    self.delete_sibling(node, i, i + 1)
                else:
                    self.delete_merge(node, i, i + 1)
            elif i + 1 == len(node.children):
                if len(node.children[i - 1].keys) >= t:
                    self.delete_sibling(node, i, i - 1)
                else:
                    self.delete_merge(node, i, i - 1)
            self.delete(node.children[i], k)

    # Delete internal node
    def delete_internal_node(self, node, k, i):
        t = self.t
        if node.leaf:
            if node.keys[i][0] == k[0]:
                node.keys.pop(i)
                return
            return

        if len(node.children[i].keys) >= t:
            node.keys[i] = self.delete_predecessor(node.children[i])
            return
        elif len(node.children[i + 1].keys) >= t:
            node.keys[i] = self.delete_successor(node.children[i + 1])
            return
        else:
            self.delete_merge(node, i, i + 1)
            self.delete_internal_node(node.children[i], k, self.t - 1)

    # Delete the predecessor
    def delete_predecessor(self, node):
        if node.leaf:
            return node.pop()
        n = len(node.keys) - 1
        if len(node.children[n].keys) >= self.t:
            self.delete_sibling(node, n + 1, n)
        else:
            self.delete_merge(node, n, n + 1)
        self.delete_predecessor(node.children[n])

    # Delete the successor
    def delete_successor(self, node):
        if node.leaf:
            return node.keys.pop(0)
        if len(node.children[1].keys) >= self.t:
            self.delete_sibling(node, 0, 1)
        else:
            self.delete_merge(node, 0, 1)
        self.delete_successor(node.children[0])

    # Delete resolution
    def delete_merge(self, node, i, j):
        cnode = node.children[i]

        if j > i:
            rsnode = node.children[j]
            cnode.keys.append(node.keys[i])
            for k in range(len(rsnode.keys)):
                cnode.keys.append(rsnode.keys[k])
                if len(rsnode.children) > 0:
                    cnode.children.append(rsnode.children[k])
            if len(rsnode.children) > 0:
                cnode.children.append(rsnode.children.pop())
            new = cnode
            node.keys.pop(i)
            node.children.pop(j)
        else:
            lsnode = node.children[j]
            lsnode.keys.append(node.keys[j])
            for i in range(len(cnode.keys)):
                lsnode.keys.append(cnode.keys[i])
                if len(lsnode.children) > 0:
                    lsnode.children.append(cnode.children[i])
            if len(lsnode.children) > 0:
                lsnode.children.append(cnode.children.pop())
            new = lsnode
            node.keys.pop(j)
            node.children.pop(i)

        if node == self.root and len(node.keys) == 0:
            self.root = new

    # Delete the sibling
    def delete_sibling(self, node, i, j):
        cnode = node.children[i]
        if i < j:
            rsnode = node.children[j]
            cnode.keys.append(node.keys[i])
            node.keys[i] = rsnode.keys[0]
            if len(rsnode.children) > 0:
                cnode.children.append(rsnode.children[0])
                rsnode.children.pop(0)
            rsnode.keys.pop(0)
        else:
            lsnode = node.children[j]
            cnode.keys.insert(0, node.keys[i - 1])
            node.keys[i - 1] = lsnode.keys.pop()
            if len(lsnode.children) > 0:
                cnode.children.insert(0, lsnode.children.pop())
    
tree = BTree(3)

for i in range(10):
    tree.addNode(i)

tree.printtree()

if tree.search_key(10) is not None:
    print("\nFound")
else:
    print("\nNot Found")