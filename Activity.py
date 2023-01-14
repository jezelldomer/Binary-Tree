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
        
    #••••••••This is for the exercise part••••••••
    
    #function for post order traversal
    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

    #function for pre order traversal
    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements
      
    #function for finding the max data      
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    #function for finding the min data
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
        
    #function for deleting elements      
    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left        

    
def build_tree(elements):
    print("ི⋮ ྀ⏝ ི⋮ ྀ⏝ ི⋮ ྀ⏝ ི⋮ ྀ⏝ ི⋮ ྀ⏝ ི⋮ ྀ⏝ ི⋮ ྀ⏝ ི⋮ ྀ⏝ ི⋮ ྀ\n")
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':
    letters = ["J","E","Z", "E","L","L","D","O","M","E","R"] #elements
    
    #for printing the search elements
    letter_tree = build_tree(letters)
    print("Building tree with the elements below", "\nLetters of my Full Name:")
    print (letters,"\n")
    print("E is in the list? ", letter_tree.search("E"))
    print("P is in the list? ", letter_tree.search("P"))
        
    print("\nMin:",letter_tree.find_min())
    print("Max:",letter_tree.find_max())
    
    #for printing the order traversal
    print("\nIn-order traversal:", letter_tree.in_order_traversal())
    print("Pre-order traversal:", letter_tree.pre_order_traversal())
    print("Post-order traversal:", letter_tree.post_order_traversal(),"\n")
    
    #for deleting an element
    numbers = [18, 17, 4, 1, 9, 20, 25, 88] 
    numbers_tree = build_tree(numbers)
    numbers_tree.delete(20)
    print("New Set of Elements:")
    print(numbers)
    print("\nAfter deleting 20 ",numbers_tree.in_order_traversal()) 
    
               
    print("\nི⋮ ྀ⏝ ི⋮ ྀ⏝ ི⋮ ྀ⏝ ི⋮ ྀ⏝ ི⋮ ྀ⏝ ི⋮ ྀ⏝ ི⋮ ྀ⏝ ི⋮ ྀ⏝ ི⋮ ྀ")
    
