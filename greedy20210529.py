# 민식이는 수학학원에서 단어 수학 문제를 푸는 숙제를 받았다.

# 단어 수학 문제는 N개의 단어로 이루어져 있으며, 각 단어는 알파벳 대문자로만 이루어져 있다. 
# 이때, 각 알파벳 대문자를 0부터 9까지의 숫자 중 하나로 바꿔서 N개의 수를 합하는 문제이다. 
# 같은 알파벳은 같은 숫자로 바꿔야 하며, 두 개 이상의 알파벳이 같은 숫자로 바뀌어지면 안 된다.

# 예를 들어, GCF + ACDEB를 계산한다고 할 때, A = 9, B = 4, C = 8, D = 6, E = 5, F = 3, G = 7로 결정한다면, 
# 두 수의 합은 99437이 되어서 최대가 될 것이다.

# N개의 단어가 주어졌을 때, 그 수의 합을 최대로 만드는 프로그램을 작성하시오.

# GCF + ACDEB를 계산한다고 할 때, A = 9, B = 4, C = 8, D = 6, E = 5, F = 3, G = 7
# N = int(input())


# numbers = ['9', '4', '8', '6', '5', '3', '7']
# alpabets = ['A', 'B', 'C', 'D','E','F', 'G']
# arr = []


# for i in range(N):
#   a = input()
#   for i2 in range(len(alpabets)):
#     a = a.replace(alpabets[i2], numbers[i2])
#   arr.append(int(a))
# print(sum(arr))

# 시간 초과 뜸 런타임 에러

# dictionary = {'A' : '9', 'B' : '4', 'C' : '8', 'D' : '6','E' : '5','F' : '3', 'G' : '7'}

# for i in range(N):
#   a = input()
#   transTable = a.maketrans(dictionary)
#   a = a.translate(transTable)
#   arr.append(int(a))
# print(sum(arr))

# 이거도 런타임 에러가 난다


# 생각을 잘못했다
# 그냥 자리 수가 많은 거에 큰 수를 줘야 한다
#n입력받기
n=int(input())

#단어 입력받을 리스트 만들기
words=[]

#단어 입력받기
for i in range(n):
  words.append(input())

#딕셔너리 초기화하기
dict={}
#딕셔너리에 알파벳당 숫자 집어넣기
for word in words:
  k=len(word)-1
  for s in word:
    if s in dict:
      dict[s]+=pow(10,k)
    else:
      dict[s]=pow(10,k)
    k-=1

#숫자 리스트 초기화하기
nums=[]

#사전의 값들만으로 이루어진 리스트 초기화하기
for value in dict.values():
  nums.append(value)

#숫자 큰순으로 정렬하기
nums.sort(reverse=True)

#출력할 값과 곱해야하는 수 초기화하기
result,t=0,9

#값 구하기
for i in range(len(nums)):
  result+=nums[i]*t
  t-=1

print(result)

