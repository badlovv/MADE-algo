import sys


class Node:

    def __init__(self, key: int, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


class BST:

    def __init__(self):
        self.root = None

    def insert(self, x, v='root'):
        if v == 'root':
            if self.root is None:
                self.root = Node(x)
                return self.root
            return self.insert(x, self.root)
        if v is None:
            return Node(x)
        elif x < v.key:
            v.left = self.insert(x, v.left)
        elif x > v.key:
            v.right = self.insert(x, v.right)
        return v

    def exists(self, x, v='root'):
        if v == 'root':
            if self.root is None:
                return 'false'
            return self.exists(x, self.root)
        if v is None:
            return 'false'
        if v.key == x:
            return 'true'
        elif x < v.key:
            return self.exists(x, v.left)
        else:
            return self.exists(x, v.right)

    def delete(self, x, v='root'):
        if v == 'root':
            if self.root is None:
                return self.root
            self.root = self.delete(x, self.root)
            return
        if v is None:
            return None
        # print(x, v.key, v.left, v.right)
        if x < v.key:
            v.left = self.delete(x, v.left)
        elif x > v.key:
            v.right = self.delete(x, v.right)
        elif v.right is None and v.left is None:
            v = None
        elif v.left is None:
            v = v.right
        elif v.right is None:
            v = v.left
        else:
            v.key = self.find_max(v.left).key
            v.left = self.delete(v.key, v.left)
        return v

    def find_max(self, v):
        while v.right is not None:
            v = v.right
        return v

    def next(self, x):
        if self.root is None:
            return 'none'
        v = self.root
        next_key = 'none'
        while v is not None:
            if v.key > x:
                next_key = v.key
                v = v.left
            else:
                v = v.right
        return next_key

    def prev(self, x):
        if self.root is None:
            return 'none'
        v = self.root
        prev_key = 'none'
        while v is not None:
            if v.key < x:
                prev_key = v.key
                v = v.right
            else:
                v = v.left
        return prev_key


if __name__ == '__main__':
    arr = sys.stdin.readlines()
    arr = [el.split() for el in arr]
    bst = BST()
    for op in arr:
        x = int(op[1])
        if op[0] == 'insert':
            bst.insert(x)
        elif op[0] == 'exists':
            print(bst.exists(x))
        elif op[0] == 'delete':
            bst.delete(x)
        elif op[0] == 'next':
            print(bst.next(x))
        else:
            print(bst.prev(x))



"""
insert 2
insert 5
insert 3
delete 2
delete 3
delete 5
exists 2
exists 4
next 4
prev 4
delete 5
delete 5
exists 5
insert 5
exists 5
prev 5
next 4
next 5
prev 4


true
false
5
3
none
3
"""

