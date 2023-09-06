function solution(N, stages) {
  // 시간 복잡도가 N * stages 이므로 500 * 200,000 = 10,000^2, 즉 2중 for문 불가능

  let dict = {}; // dict : 각 stage에 위치한 유저 수를 value로 저장하기 위한 객체

  for (const stage of stages) {
    if (stage in dict) {
      dict[stage] += 1;
    } else {
      dict[stage] = 1;
    }
  }

  let preUserCnt = 0; // preUserCnt : stage1부터 한 stage씩 증가하면서 더하기 누적된 유저 수
  let failRate = {}; // failRate : 각 stage의 실패율 저장하기 위한 객체

  // 1부터 N까지 각 stage의 실패율 구하기
  for (let stage = 1; stage <= N; stage++) {
    // 실패율 = 클리어 못한 유저 수 / 스테이지 도달한 유저 수
    // = 현재 stage에 있는 유저 수(dict[stage]) / (총 유저 수(stages.length) - preUserCnt)
    if (stage in dict) {
      failRate[stage] = dict[stage] / (stages.length - preUserCnt);
      preUserCnt += dict[stage];
    } else {
      // 해당 stage에 있는 유저 없는 경우 실패율은 0
      failRate[stage] = 0;
    }
  }

  // 실패율 높은 스테이지 번호부터 내림차순, 실패율 같으면 작은 번호부터
  let sortedArray = [];
  for (const key in failRate) {
    sortedArray.push([parseInt(key), failRate[key]]); // [stage값, 실패율]
  }

  sortedArray.sort((a, b) => {
    return b[1] - a[1];
  });

  // 실패율 1등이 최종 stage까지 다 깬 N + 1 인 경우 제외
  let answer = [];
  if (parseInt(sortedArray[0][0]) === N + 1) {
    for (let i = 1; i < sortedArray.length; i++) {
      answer.push(sortedArray[i][0]);
    }
  } else {
    for (let i = 0; i < sortedArray.length; i++) {
      answer.push(sortedArray[i][0]);
    }
  }

  return answer;
}
