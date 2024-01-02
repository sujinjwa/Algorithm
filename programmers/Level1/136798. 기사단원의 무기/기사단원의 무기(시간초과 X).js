function solution(number, limit, power) {
  // 1. 갹 기사 번호의 약수 개수 구하기
  const count = {};

  for (let i = 1; i <= number; i++) {
    // i의 약수 개수 구하기

    let cnt = 0;
    // 내부 for문을 j가 i / 2 + 1일 때까지가 아니라 Math.sqrt(i) 일 때까지만 진행
    for (let j = 1; j <= Math.sqrt(i); j++) {
      if (j === Math.sqrt(i)) cnt += 1;
      else if (i % j === 0) cnt += 2;
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
