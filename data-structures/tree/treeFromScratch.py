
class Node :
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
    def insert_node(self,value):
        if self.value:
            if value< self.data:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.insert_node(value)
            elif value> self.data:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.insert_node(value)
        else:
            self.value = value
