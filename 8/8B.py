import sys


class Node:

    def __init__(self, key: int, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
        self.h = 1


class AVLBST:

    def __init__(self):
        self.root = None

    def fix(self, v):
        if v.right is None and v.left is None:
            v.h = 1
        elif v.left is None:
            v.h = v.right.h + 1
        elif v.right is None:
            v.h = v.left.h + 1
        else:
            v.h = max(v.left.h, v.right.h) + 1

    def node_balance(self, v):
        if v.right is None and v.left is None:
            return 0
        elif v.left is None:
            return v.right.h
        elif v.right is None:
            return 0 - v.left.h
        else:
            return v.right.h - v.left.h

    def balance(self, v):
        if v is None:
            return v
        self.fix(v)
        b = self.node_balance(v)
        if b == 2:
            if self.node_balance(v.right) < 0:
                v.right = self.small_rotate(v.right, 'right')
            return self.small_rotate(v, 'left')
        elif b == - 2:
            if self.node_balance(v.left) > 0:
                v.left = self.small_rotate(v.left, 'left')
            return self.small_rotate(v, 'right')
        return v

    def small_rotate(self, p, how):
        if how == 'right':
            q = p.left
            p.left = q.right
            q.right = p
        else:
            q = p.right
            p.right = q.left
            q.left = p
        if q.left == self.root or q.right == self.root:
            self.root = q
        self.fix(p)
        self.fix(q)
        return q

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
        return self.balance(v)

    def delete(self, x, v='root'):
        if v == 'root':
            if self.root is None:
                return self.root
            self.root = self.delete(x, self.root)
            return
        if v is None:
            return None
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
        return self.balance(v)

    def find_max(self, v):
        while v.right is not None:
            v = v.right
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

    def print_tree(self, v='root'):
        if v == 'root':
            self.print_tree(self.root)
            return
        if v is not None:
            self.print_tree(v.left)
            print(v.key, end=' ')
            self.print_tree(v.right)
        return v


if __name__ == '__main__':
    arr = sys.stdin.readlines()
    arr = [el.split() for el in arr]
    bst = AVLBST()
    res = []
    for op in arr:
        x = int(op[1])
        if op[0] == 'insert':
            bst.insert(x)
        elif op[0] == 'exists':
            # print(bst.exists(x))
            res.append(bst.exists(x))
        elif op[0] == 'delete':
            bst.delete(x)
        elif op[0] == 'next':
            res.append(bst.next(x))
        else:
            res.append(bst.prev(x))
    print('\n'.join(map(str, res)))



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

