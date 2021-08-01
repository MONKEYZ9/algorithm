# Python 2, Python 3, PyPy, PyPy3: def solve(a: list) -> int
# a: 합을 구해야 하는 정수 n개가 저장되어 있는 리스트 (0 ≤ a[i] ≤ 1,000,000, 1 ≤ n ≤ 3,000,000)
# 리턴값: a에 포함되어 있는 정수 n개의 합 (정수)
# def get_hab(a):
#     return sum(a)
def get_notd(n):
    new_list = []
    for i in range(n):
        string_n = str(i)
        if len(string_n) < 2:
            string_n = '0' + string_n
            i += i + int(string_n[0]) + int(string_n[1])
            new_list.append(i)
            print(new_list)

        else:
            i += i + int(string_n[0]) + int(string_n[1])
            new_list.append(i)
            print(new_list)
        return new_list
def d(n):
    new_list = get_notd(n)
    if n not in new_list:
        return n

n_list = []
# for i in range(1, 10):
get_notd(5)


# 1 1+1 2
# 2 2+2 4
# 3 3+3 6
# 4 4+4 8
# 5 5+5 10
# 6 6+6 12
# 7 7+7 14
# 8 8+8 16
# 9 9+9 18
# 10 10 + 1 + 0 = 11
# 11 11+1+1 13
# 12 12+1+2 15
# 13 13+1+3 17
# 14 14+1+4 19
# 15 15+1+5 21
# 31 31+3+1 35