import sys

n = int(input()) # 높이가 0 ~ 100까지인 언덕 개수
heights = [
    int(input())
    for _ in range(n)
]

# 가장 낮은 언덕의 높이 i 일 경우,
# 언덕의 높이차 17 이하 되도록 만드는 비용 구하기
min_cnt = sys.maxsize
for i in range(84): # 언덕 최대 높이 100 이므로, 최소 높이는 100 - 17까지만 가능
    
    cnt = 0 # 가장 낮은 언덕의 높이 i일 때의 각 비용
    for height in heights:
        # 해당 언덕의 높이가 i보다 낮을 경우
        if height < i:
            cnt += (i - height) * (i - height)

        # 해당 언덕의 높이가 i + 17보다 높을 경우
        if i + 17 < height:
            max_height = i + 17
            cnt += (max_height - height) * (max_height - height)
    
    min_cnt = min(min_cnt, cnt) # 최소 비용 구하기

print(min_cnt)