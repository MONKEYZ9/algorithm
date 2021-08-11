n = int(input())
for _ in range(n):
    word = input()
    for i in range(1, len(word)):
        if word.find(word[i-1]) > word.find(word[i]):
            n -= 1 
            break
print(n)
