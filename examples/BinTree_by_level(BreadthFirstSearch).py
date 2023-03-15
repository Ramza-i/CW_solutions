class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

    def __repr__(self):
        return f'(L={self.left} R={self.right} Val={self.value})'

# b = Node(Node(None, Node(None, None, 5), 3), Node(Node(None, None, 6), Node(None, None, 7), 4), 2)
b= []

def tree_by_levels(node):
    res = []
    for i in range(height(node)):
        print_level(node, res, i)
    return res

def print_level(node, res, level):
    if not node:
        return
    if level == 0:
        res.append(node.value)
    if level > 0:
        print_level(node.left, res, level - 1)
        print_level(node.right, res, level - 1)

def height(node):
    if not node:
        return 0
    Lnodeh = height(node.left)
    Rnodeh = height(node.right)
    return max(Lnodeh, Rnodeh) + 1

# print(tree_by_levels(b))

def test(node):
    if not node:
        return []
    p, q = [], [node]
    print(f'q -- {q}')
    while q:
        v = q.pop(0)
        if v:
            p.append(v.value)
            q += [v.left,v.right]
    return p

print(test(b))