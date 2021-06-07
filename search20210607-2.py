# 음료수 얼려먹기
n, m = map(int, input().split())

dataN = []

for i in range(n):
    dataN.append(list(map(int, input())))

def dfs(x, y):
    if x <= -1 or x>=n or y <= -1 or y >= m:
        return False
    if dataN[x][y] == 0:
        # 해당 위치를 방문했다고 표시해주고
        dataN[x][y] = 1
        # 상하좌우는 재귀함수를 통해서 반복해서 확인해주자
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return True

    return False
# 모든 노드 위치에 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 여기서 dfs 실행하기
        if dfs(i, j) == True:
            result += 1
print(result)

