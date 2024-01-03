function solution(babbling) {
  let answer = 0;
  const says = ['aya', 'ye', 'woo', 'ma'];

  // babbling를 조회하면서
  // 각 word의 알파벳 하나씩 temp에 추가하면서
  // temp가 4가지 발음 중 하나면 temp 초기화하는 과정 반복
  // 결과적으로 temp가 빈 문자열이면 옹알이 성공
  babbling.forEach((bab) => {
    let temp = '';
    let preTemp = '';
    Array.from(bab).forEach((b) => {
      temp += b;

      // 이전에 옹알이한 단어를 이번에 또 옹알이하려는 경우는 포함 X
      if (says.includes(temp) && preTemp !== temp) {
        preTemp = temp;
        temp = '';
      }
    });

    if (temp.length === 0) {
      answer += 1;
    }
  });

  return answer;
}
