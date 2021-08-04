N = int(input())
N_list = list(map(int, (input().split())))

max_score = max(N_list)
new_num = [num/max_score*100 for num in N_list]

new_avg = sum(new_num)/len(new_num)
print(new_avg)