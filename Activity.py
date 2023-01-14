class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    #function for child in data
    def add_child(self, data):
        if data == self.data:
            return # node already exist

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    #function for searching elements
    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
                
    #function for in order traversal
    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements


def build_tree(elements):
    print("Building tree with these elements,", "letters of my Full Name:",elements,"\n")
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':
    letters = ["J","E","Z", "E","L","L","D","O","M","E","R"] #elements
    
    #for printing the search elements
    letter_tree = build_tree(letters)
    print("E is in the list? ", letter_tree.search("E"))
    print("P is in the list? ", letter_tree.search("P"))
    #for printing the order traversal
    print("\nIn order traversal gives this sorted list:",letter_tree.in_order_traversal())