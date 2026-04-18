from collections import defaultdict

d=lambda: defaultdict(d)
tree=defaultdict(d)

for _ in range(int(input())):
    inp = input().split()[1:]
    cur = tree
    for i in inp:
        cur = cur[i]

def print_tree(tree, depth):
    for i in sorted(tree.keys()):
        print(('--' * depth) + i)
        print_tree(tree[i], depth + 1)

print_tree(tree, 0)