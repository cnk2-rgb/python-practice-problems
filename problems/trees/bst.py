class Empty:

    def __init__(self):
        # nothing to do!
        pass

    @property
    def is_empty(self):
        return True

    @property
    def is_leaf(self):
        return False

    def num_nodes(self):
        return 0

    def height(self):
        return 0

    def contains(self, n):
        return False

    def insert(self, n):
        return Node(n, Empty(), Empty())


class Node:

    def __init__(self, n, left, right):
        self.value = n
        self.left = left
        self.right = right

    @property
    def is_empty(self):
        return False

    @property
    def is_leaf(self):
        return self.left.is_empty and self.right.is_empty

    def num_nodes(self):
        return 1 + self.left.num_nodes() + self.right.num_nodes()

    def height(self):
        return 1 + max(self.left.height(), self.right.height())

    def contains(self, n):
        if n < self.value:
            return self.left.contains(n)
        elif n > self.value:
            return self.right.contains(n)
        else:
            return True

    def inorder(self):
        #print(self.height())
        #print(self.value)
        if self.is_leaf:
            print("entering base")
            return [self.value]
        else:
            print("entering recursive case")
            if not self.left.is_empty:
                print("entering left case")
                print(self.value)
                left = self.left.inorder() + [self.value]
            else:
                left = []
            if not self.right.is_empty:
                print("entering right...")
                right = self.right.inorder()
            else:
                right = []
            print(left + right)
            return left + right
            
            

    def min_item(self):
        if self.left.is_empty:
            return self.value
        return self.left.min_item()

    def max_item(self):
        if self.right.is_empty:
            return self.value
        return self.right.max_item()

    def balance_factor(self):
        right_height = self.right.height()
        left_height = self.left.height()

        return right_height - left_height

    def balanced_everywhere(self):
        self.balance_factor()


    def insert(self, n):
        if n < self.value:
            return Node(self.value, self.left.insert(n), self.right)
        elif n > self.value:
            return Node(self.value, self.left, self.right.insert(n))
        else:
            return self


if __name__ == "__main__":
    bst = Empty().insert(42).insert(10).insert(15).insert(63)

    print(f"The number of nodes is {bst.num_nodes()}")
    print(f"The height is {bst.height()}")