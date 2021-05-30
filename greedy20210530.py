N = int(input())

card = []
for i in range(N):
    card.append(int(input()))

card.sort()

answers = []
answer = 0
for i in range(N):
    answer += card[i]
    # 10 30 70
    answers.append(answer)
print(answers[-1] + answers[-2])
