x_list = []
y_list = []
for _ in range(3):
    x, y = map(int,(input().split()))
    x_list.append(x)
    y_list.append(y)

set_x_list = list(set(x_list))
set_y_list = list(set(y_list))

x1 = x_list.count(set_x_list[0])
x2 = x_list.count(set_x_list[1])
y1 = y_list.count(set_y_list[0])
y2 = y_list.count(set_y_list[1])


if x1 == 1:
    if y1 == 1:
        print(set_x_list[0],set_y_list[0])
    else:
        print(set_x_list[0],set_y_list[1])
else:
    if y1 == 1:
        print(set_x_list[1],set_y_list[0])
    else:
        print(set_x_list[1],set_y_list[1])