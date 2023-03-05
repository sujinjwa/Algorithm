def solution(periods, payments, estimates):
    # 가입 기간 (1차원): periods
    # 최근 12개월 간 납부 내역 (2차원): payments
    # 납부 예정 금액 (1차원) : estimates
    # 다음 달 vip 되는 고객 수 : willbeVIP
    # 다음 달 vip 아니게 되는 고객 수 : wasVip

    willbeVIP = 0
    wasVIP = 0
    for i in range(len(periods)): # 모든 고객 조회
        # i := i+1번 고객
        
        if periods[i] < 23: # 2년 미만일 경우 vip였지도 x, vip 되지도 x
            continue

        year_payment = 0 # 금액
        for j in range(12): # i+1번 고객의 최근 12개월 납부 금액 조회
            year_payment += payments[i][11-j] # 연간 납부 금액 총합
        
        # 다음 달 새 연간 납부 금액 총합
        new_year_payment = year_payment - payments[i][0] + estimates[i]

        # 가입 기간이 이제 2년 이상 되어, willbeVIP인 경우
        if year_payment < 900000 and periods[i] < 59:
            if new_year_payment >= 900000: # 이번 달 vip 된다면
                willbeVIP += 1
                print(i, new_year_payment)
        
        # 가입 기간이 2년 이상 되어, willbeVIP인 경우
        if periods[i] == 23 and new_year_payment >= 900000:
            willbeVIP += 1
        
        # 가입 기간이 5년 미만인데, wasVIP인 경우
        if year_payment >= 900000 and periods[i] < 59:
            if new_year_payment < 900000:
                wasVIP += 1
                print(i, new_year_payment)
        
        # 가입 기간 5년 이상인데, willbeVIP인 경우
        if periods[i] >= 59 and year_payment < 600000:
            if new_year_payment >= 600000:
                willbeVIP += 1
                print(i, new_year_payment)
        
        # 가입 기간이 이제 5년 이상되어, willbVIP인 경우
        if periods[i] == 59 and new_year_payment >= 600000:
            willbeVIP += 1

        # 가입 기간 5년 이상인데, wasVIP인 경우
        if periods[i] >= 59 and year_payment >= 600000:
            if new_year_payment < 600000:
                wasVIP += 1
                print(i, new_year_payment)

    answer = []
    answer.append(willbeVIP)
    answer.append(wasVIP)
    return answer