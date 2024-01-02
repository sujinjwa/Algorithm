function solution(number, limit, power) {
  // 1. 갹 기사 번호의 약수 개수 구하기
  const count = {};

  for (let i = 1; i <= number; i++) {
    // i의 약수 개수 구하기
    let cnt = 1;
    for (let j = 2; j <= i; j++) {
      if (i % j === 0) cnt += 1;
    }

    count[i] = cnt;
  }

  // 2. 약수 개수 중 제한수치보다 높으면 +power, 아니면 +개수
  let answer = 0;

  Object.entries(count).forEach(([num, cnt]) => {
    if (cnt > limit) answer += power;
    else answer += cnt;
  });

  return answer;
}
