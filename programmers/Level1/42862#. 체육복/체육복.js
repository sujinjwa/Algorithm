function solution(n, lost, reserve) {
  let answer = 0;

  // 1. n 중에 lost 아닌 애들만 카운트
  answer += n - lost.length;

  reserve.sort(); // 오름차순 정렬되어있지 않으면 발생하는 에러 해결 위함

  // 2. reserve 중에 lost에 해당되는 사람 있으면 카운트 + 1 해주고 reserve에서 지우기
  temp = [];
  reserve.forEach((num) => {
    if (lost.includes(num)) {
      answer += 1;
      lost = lost.filter((num2) => num2 !== num);
    } else {
      temp.push(num);
    }
  });
  reserve = temp;

  lost.sort(); // 오름차순 정렬되어있지 않으면 발생하는 에러 해결 위함

  // 3. reserve 중에 lost의 앞, 뒤에 해당되는 사람 있으면 카운트 + 1 해주기
  lost.forEach((num) => {
    if (reserve.includes(num - 1)) {
      answer += 1;
      reserve = reserve.filter((num2) => num2 !== num - 1);
      return;
    }

    if (reserve.includes(num + 1)) {
      answer += 1;
      reserve = reserve.filter((num2) => num2 !== num + 1);
      return;
    }
  });

  return answer;
}
