# 민식이는 수학학원에서 단어 수학 문제를 푸는 숙제를 받았다.

# 단어 수학 문제는 N개의 단어로 이루어져 있으며, 각 단어는 알파벳 대문자로만 이루어져 있다. 
# 이때, 각 알파벳 대문자를 0부터 9까지의 숫자 중 하나로 바꿔서 N개의 수를 합하는 문제이다. 
# 같은 알파벳은 같은 숫자로 바꿔야 하며, 두 개 이상의 알파벳이 같은 숫자로 바뀌어지면 안 된다.

# 예를 들어, GCF + ACDEB를 계산한다고 할 때, A = 9, B = 4, C = 8, D = 6, E = 5, F = 3, G = 7로 결정한다면, 
# 두 수의 합은 99437이 되어서 최대가 될 것이다.

# N개의 단어가 주어졌을 때, 그 수의 합을 최대로 만드는 프로그램을 작성하시오.

# GCF + ACDEB를 계산한다고 할 때, A = 9, B = 4, C = 8, D = 6, E = 5, F = 3, G = 7
N = int(input())


numbers = ['9', '4', '8', '6', '5', '3', '7']
alpabets = ['A', 'B', 'C', 'D','E','F', 'G']
arr = []


# for i in range(N):
#   a = input()
#   for i2 in range(len(alpabets)):
#     a = a.replace(alpabets[i2], numbers[i2])
#   arr.append(int(a))
# print(sum(arr))

# 시간 초과 뜸 런타임 에러

dictionary = {'A' : '9', 'B' : '4', 'C' : '8', 'D' : '6','E' : '5','F' : '3', 'G' : '7'}

for i in range(N):
  a = input()
  transTable = a.maketrans(dictionary)
  a = a.translate(transTable)
  arr.append(int(a))
print(sum(arr))

# 이거도 런타임 에러가 난다
