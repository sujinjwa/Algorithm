function solution(s) {
  let answer = 0;

  while (s.length >= 1) {
    if (s.length === 1) {
      answer += 1;
      break;
    }

    // 1. 첫 글자 구하기
    const firstWord = s[0];

    // 2. 횟수 세기
    let cnt1 = 0;
    let cnt2 = 0;
    let find = false;
    for (let i = 0; i < s.length; i++) {
      if (s[i] === firstWord) cnt1 += 1;
      else cnt2 += 1;

      if (cnt1 === cnt2) {
        s = s.substring(i + 1, s.length);
        answer += 1;
        find = true;
        break;
      }
    }

    // 두 횟수 다른 상태에서 더 이상 읽을 글자 없으면 분리하고 종료
    if (!find) {
      answer += 1;
      break;
    }
  }

  return answer;
}
