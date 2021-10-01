from collections import Counter
import sys

N = int(sys.stdin.readline())
N_list = [int(sys.stdin.readline()) for _ in range(N)]
print(round(sum(N_list)/len(N_list)))
print((N_list[len(N_list)//2]))
cnt_li = Counter(N_list).most_common()
if len(cnt_li) > 1 and cnt_li[0][1]==cnt_li[1][1]: #최빈값 2개 이상
    print(cnt_li[1][0])
else:
    print(cnt_li[0][0])
print(max(N_list)-min(N_list))
