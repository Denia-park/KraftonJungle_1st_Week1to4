class Node:
    """
    이진 검색 트리의 노드
    """

    def __init__(self, key, value, left=None, right=None):
        """
        생성자
        """
        self.key = key  # 키
        self.value = value  # 값
        self.left = left  # 왼쪽 포인터
        self.right = right  # 오른쪽 포인터


class BinarySearchTree:
    """
    이진 검색 트리
    """

    def __init__(self):
        """
        초기화
        """
        self.root = None  # 루트

    def search(self, key):
        """키가 key인 노드를 검색"""

        cur_node = self.root  # 루트에 주목
        while True:
            if cur_node is None:  # 더 이상 진행할 수 없으면
                return None  # 검색 실패
            if key == cur_node.key:  # key 와 노드 cur_node의 키가 같으면
                return cur_node.value
            elif key < cur_node.key:  # key 쪽이 작으면
                cur_node = cur_node.left  # 왼쪽 서브트리에서 검색
            else:
                cur_node = cur_node.right  # 오른쪽 서브트리에서 검색

    def add(self, key, value):
        """
        키가 key이고 값이 value인 노드를 삽입
        """

        def add_node(node, key, value):
            """
            node를 루트로 하는 서브트리에 키가 key이고 값이 value인 노드를 삽입
            """
            if key == node.key:
                return False  # Key가 이진 검색 트리에 이미 존재
            elif key < node.key:
                if node.left is None:
                    node.left = Node(key, value, None, None)
                else:
                    add_node(node.left, key, value)
            else:
                if node.right is None:
                    node.right = Node(key, value, None, None)
                else:
                    add_node(node.right, key, value)

            return True

        if self.root is None:
            self.root = Node(key, value, None, None)
            return True
        else:
            return add_node(self.root, key, value)

    def remove(self, key):
        """
        키가 key인 노드를 삭제
        """
        cur_node = self.root  # 현재 스캔중인 노드
        parent = None  # 스캔 중인 노드의 부모 노드
        is_left_child = True  # cur_node 가 부모 노드의 왼쪽 자식 노드인지 확인

        while True:
            if cur_node is None:  # 더 이상 진행할 수 없으면
                return False  # 그 키는 존재하지 않음

            if key == cur_node.key:  # key 와 cur_node.key 가 같으면
                break  # 검색 성공
            else:
                parent = cur_node  # 가지를 타고 내려가기 전에 부모 노드를 설정
                if key < cur_node.key:  # key 값이 작으면
                    is_left_child = True  # 왼쪽 자식으로 내려가야 함
                    cur_node = cur_node.left
                else:  # key 값 쪽이 크면
                    is_left_child = False  # 오른쪽 자식으로 내려가야 함
                    cur_node = cur_node.right

        if cur_node.left is None:  # cur_node 의 왼쪽 자식이 없으면
            if cur_node is self.root:
                self.root = cur_node.right
            elif is_left_child:
                parent.left = cur_node.right  # 부모의 왼쪽 포인터가 오른쪽 자식을 가리킴
                # cur_node 의 right가 있으면 있는대로 연결 , 없으면 없는대로 None 을 연결
            else:
                parent.right = cur_node.right  # 부모의 오른쪽 포인터가 오른쪽 자식을 가리킴
        elif cur_node.right is None:
            if cur_node is self.root:
                self.root = cur_node.left
            elif is_left_child:
                parent.left = cur_node.left  # 부모의 왼쪽 포인터가 왼쪽 자식을 가리킴
            else:
                parent.right = cur_node.left  #  부모의 오른쪽 포인터가 왼쪽 자식을 가리킴

        # 위에는 자식이 없거나 1개만 있는 케이스 | 아래는 자식이 둘다 있는 케이스
        else:
            # self.root를 지우는 케이스 고려
            parent = cur_node
            left = cur_node.left
            is_left_child = True
            while left.right is not None:  # 가장 큰 노드 left를 검색하기 위해서
                parent = left  # 내려가야 하므로 parent를 저장
                left = left.right  # left 에 right를 넣는 이유는 while 루프를 위해서
                is_left_child = False  # 오른쪽으로 가니까 False

            cur_node.key = left.key  # left의 키를 cur_node 로 이동
            cur_node.value = left.value  # left의 value를 cur_node 로 이동

            if is_left_child:
                parent.left = (
                    left.left
                )  # left를 삭제한다. , left가 있건 없건 주소를 이렇게 이으면 중간에 있는 left는 삭제 됨
            else:
                parent.right = (
                    left.left
                )  # left를 삭제한다. , left가 있건 없건 주소를 이렇게 이으면 중간에 있는 left는 삭제 됨

        return True

    def dump(self):
        """
        덤프 (모든 노드를 키의 오름차순으로 출력)
        """

        def print_subtree(node):
            """
            node를 루트로 하는 서브트리의 노드를 키의 오름차순으로 출력
            """
            print_subtree(node.left)  # 왼쪽 서브트리를 오름차순으로 출력
            print(f"{node.key}  {node.value}")  # node를 출력
            print_subtree(node.right)  # 오른쪽 서브트리를 오름차순으로 출력

        print_subtree(self.root)

    def min_key(self):
        """
        가장 작은 키
        """
        if self.root is None:
            return None

        cur_node = self.root

        while cur_node.left is not None:
            cur_node = cur_node.left

        return cur_node.key

    def max_key(self):
        """
        가장 큰 키
        """
        if self.root is None:
            return None

        cur_node = self.root

        while cur_node.right is not None:
            cur_node = cur_node.right

        return cur_node.key
