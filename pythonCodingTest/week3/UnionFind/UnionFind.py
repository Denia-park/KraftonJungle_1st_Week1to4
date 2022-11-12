# 특정 원소가 속한 집합 찾기
def find_parent(parents, element):
    if parents[element] != element:
        parents[element] = find_parent(parents, parents[element])
    return parents[element]


# 두 원소가 속한 집합을 합치기
# 내 부모의 부모를 바꿔줘야 내 부모를 참조하고 있는 모든 노드들이
# 바뀐 부모를 참조하게 되면서 진정한 Union이 된다. => 부모가 제대로 바뀐다.
# 부모가 제대로 바뀌어야 두개가 합집합이 되었다고 볼 수 있다.
def union_parent(parents, ele1, ele2):
    ele1_parent = find_parent(parents, ele1)
    ele2_parent = find_parent(parents, ele2)

    if ele1_parent < ele2_parent:
        parents[ele2_parent] = ele1_parent
    else:
        parents[ele1_parent] = ele2_parent



# 노드의 개수 와 간선 (Union 연산)의 개수 입력 받기
v, e = map(int, input().split())
parents = [0] * (v + 1)  # 부모 테이블 초기화하기

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parents[i] = i

# Union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parents, a, b)

# 각 원소가 속한 집합을 출력
print("각 우너소가 속한 집합: ", end="")
for i in range(1, v + 1):
    print(find_parent(parents, i), end=" ")

print()

# 부모 테이블 내용 출력하기
print("부모 테이블: ", end="")
for i in range(1, v + 1):
    print(parents[i], end="")
