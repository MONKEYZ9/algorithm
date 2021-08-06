N = int(input())
for _ in range(N):
    test_score =list(map(int, input().split()))
    avg = sum(test_score[1:])/test_score[0]
    # print(avg)
    cnt = 0
    for i in test_score[1:]:
        if i > avg:
            cnt += 1
    print(f'{cnt/test_score[0]*100:.3f}%')
