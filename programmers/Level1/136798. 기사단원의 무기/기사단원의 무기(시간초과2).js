function solution(number, limit, power) {
  // 1. 갹 기사 번호의 약수 개수 구하기
  const count = {};

  for (let i = 1; i <= number; i++) {
    // i의 약수 개수 구하기
    let cnt = 0;
    let temp = new Set();
    // 이중for문에서 내부 for문을 절반(n/2)으로 줄임
    for (let j = 1; j <= i / 2 + 1; j++) {
      if (i % j === 0) {
        temp.add(j);
        temp.add(i / j);
      }
    }

    count[i] = temp.size;
  }

  // 2. 약수 개수 중 제한수치보다 높으면 +power, 아니면 +개수
  let answer = 0;

  Object.entries(count).forEach(([num, cnt]) => {
    if (cnt > limit) answer += power;
    else answer += cnt;
  });

  return answer;
}
