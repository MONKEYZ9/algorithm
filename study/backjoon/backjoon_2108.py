import numpy as np
from scipy import stats
from collections import Counter
N = int(input())
N_list = [int(input()) for _ in range(N)]
print(np.mean(N_list))
print(np.median(N_list))
cnt_li = Counter(N_list).most_common()
if len(cnt_li) > 1 and cnt_li[0][1]==cnt_li[1][1]: #최빈값 2개 이상
    print(cnt_li[1][0])
else:
    print(cnt_li[0][0])
print(max(N_list)-min(N_list))
