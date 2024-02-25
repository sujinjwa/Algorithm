answer = 0
sum_nums = 0

def solution(numbers, target):
    
    # choose: curr_idx 번째 숫자를 더하거나 빼는 함수
    def choose(curr_idx):
        global answer, sum_nums
        
        if curr_idx == len(numbers): # numbers 내의 모든 숫자로 연산했으면
            if sum_nums == target: # numbers 내의 모든 숫자 연산한 값이 target이면
                answer += 1
            return
        
        for i in range(2):
            if i == 0:
                sum_nums += numbers[curr_idx]        
            else:
                sum_nums -= numbers[curr_idx]
            
            choose(curr_idx + 1)
            
            if i == 0:
                sum_nums -= numbers[curr_idx]
            else:
                sum_nums += numbers[curr_idx]
        
    choose(0)
    
    return answer