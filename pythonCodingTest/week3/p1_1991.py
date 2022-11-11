import sys

"""
n = input()  #2
a = [sys.stdin.readline() for _ in range(n)]  
# a = ["1 2 3", "4 5 6"]

n = input()  #2
q = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# q = [[472], [385]]

q = list(map(int, sys.stdin.readline().split()))
# q = [1, 2, 3, 4, 5]
"""

n = int(input())
graph_infos = [list(sys.stdin.readline().split()) for _ in range(n)]
graph_infos.sort()

root_node = graph_infos[0]

answer_list = []


def preorder(root_node):
    global answer_list

    def _preorder(root_node):
        answer_list.append(root_node[0])

        if root_node[1] != ".":
            next_node_idx = ord(root_node[1]) - ord("A")

            next_node = graph_infos[next_node_idx]
            _preorder(next_node)

        if root_node[2] != ".":
            next_node_idx = ord(root_node[2]) - ord("A")

            next_node = graph_infos[next_node_idx]
            _preorder(next_node)

    answer_list = []
    _preorder(root_node)
    print("".join(answer_list))


def inorder(root_node):
    global answer_list

    def _inorder(root_node):
        if root_node[1] != ".":
            next_node_idx = ord(root_node[1]) - ord("A")

            next_node = graph_infos[next_node_idx]
            _inorder(next_node)

        answer_list.append(root_node[0])

        if root_node[2] != ".":
            next_node_idx = ord(root_node[2]) - ord("A")

            next_node = graph_infos[next_node_idx]
            _inorder(next_node)

    answer_list = []
    _inorder(root_node)
    print("".join(answer_list))


def postorder(root_node):
    global answer_list

    def postorder(root_node):
        if root_node[1] != ".":
            next_node_idx = ord(root_node[1]) - ord("A")

            next_node = graph_infos[next_node_idx]
            postorder(next_node)

        if root_node[2] != ".":
            next_node_idx = ord(root_node[2]) - ord("A")

            next_node = graph_infos[next_node_idx]
            postorder(next_node)

        answer_list.append(root_node[0])

    answer_list = []
    postorder(root_node)
    print("".join(answer_list))


preorder(root_node)
inorder(root_node)
postorder(root_node)
