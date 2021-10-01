n_list = [int(input()) for _ in range(10)]


namugi_list = [
    num%42
    for num in n_list
]
namugi_list_set = set(namugi_list)
namugi_list = list(namugi_list_set)
print(len(namugi_list))