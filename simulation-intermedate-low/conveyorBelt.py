n, t = list(map(int, input().split())) # 벨트 위아래 숫자 개수: n개, 흐르는 시간: t초

up = list(map(int, input().split())) # 컨테이너 벨트 위의 숫자들
down = list(map(int, input().split())) # 컨테이너 벨트 아래의 숫자들

# 1초에 한번씩 회전할 때 t초 후의 위치 확인
for _ in range(t):
    temp1 = up[n - 1]
    temp2 = down[n - 1]
		
		# up 리스트의 가장 끝 숫자부터 앞으로 오며 한칸씩 뒤로 이동 
    for i in range(n - 1, 0, -1):
        up[i] = up[i - 1]

    up[0] = temp2 # up 리스트의 가장 앞 숫자를 temp2로 업데이트

		# down 리스트의 가장 끝 숫자부터 앞으로 오며 한칸씩 뒤로 이동
		# 그림 상으로는 가장 앞 숫자부터 뒤로 가며 한칸씩 앞으로 이동하는 것처럼 보임
    for i in range(n - 1, 0, -1):
        down[i] = down[i - 1]
    
    down[0] = temp1 # down 리스트의 가장 앞 숫자를 temp1로 업데이트

# t초 후 숫자들의 위치 출력
for elem in up:
    print(elem, end=' ')

print()

for elem in down:
    print(elem, end=' ')