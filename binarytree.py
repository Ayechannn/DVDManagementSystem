

class CustomerBinaryTree:
    def __init__(self, root=None):
        self.data = root
        self.leftNode = None
        self.rightNode = None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.leftNode is None:
                    self.leftNode = CustomerBinaryTree(data)
                else:
                    self.leftNode.insert(data)
            elif data > self.data:
                if self.rightNode is None:
                    self.rightNode = CustomerBinaryTree(data)
                else:
                    self.rightNode.insert(data)
        else:
            self.data = data

    def printBinarytree(self):
        if self.leftNode:
            self.leftNode.printBinarytree()

        print(self.data)

        if self.rightNode:
            self.rightNode.printBinarytree()

    def search(self, key):
        if self.data is None or self.data.get_accountNo() == key:
            return self.data

        elif self.data.get_accountNo() > key:
            if self.leftNode:
                return self.leftNode.search(key)
        elif self.data.get_accountNo() < key:
            if self.rightNode:
                return self.rightNode.search(key)
        else:
            return None
