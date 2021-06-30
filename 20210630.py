
# 일단, 수업시간에 하는 것만으로는 코테에 통과하는 것은 욕심이라고 하신다.
# 그럼 어떻게 해야 할까? => 과제를 잘 따라가고 추가적으로 문제를 푸는 것이 좋다고 하신다.

# 그러나 저러나 공사장 문제
# 받아야 하는 인풋 값부터 정리하자
def test2():
    a, b, R = map(int, (input().split()))
    work_position = [a, b]
    N = int(input())
    shadow_position = []
    for i  in range(N):
        x_i, y_i = map(int, input().split())
        shadow_position.append([x_i, y_i])
    # 일단 받아서 확인할 건 다했고 
    # 위치가 공사현장으로부터 얼마나 떨어져 있는지의 공식은
    # (x-a)^2 + (y-b)^2 >= R^2
    # 위의 공식이면 된다고 한다.
    # 이는 for문과 if문을 써서 결과값을 출력해주는 것으로 하자

    # work_position과 shadow_position을 비교하면 된다.
    # (shadow_position[0][0]-work_position[0])**2 - (shadow_position[0][0]-work_position[0])**2

    for i in range(len(shadow_position)):
        distance = (shadow_position[i][0]-work_position[0])**2 + (shadow_position[i][1]-work_position[1])**2
        if distance >= R**2:
            print('silent')
        else : 
            print('noisy')

test2()

# 아니 이게 왜 알고리즘 문제인거지
# 그냥 코드로 정리한거잖아

