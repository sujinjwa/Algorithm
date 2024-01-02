function solution(survey, choices) {
  const score = {
    R: 0,
    T: 0,
    C: 0,
    F: 0,
    J: 0,
    M: 0,
    A: 0,
    N: 0,
  };

  // 1. survey 조회하며, choices[i]가 1~3이면 첫번째 캐릭터에 점수 + , 5~7이면 두번째 캐릭터에 점수 +
  survey.forEach((elem, index) => {
    const first = elem[0];
    const second = elem[1];

    if (choices[index] >= 1 && choices[index] <= 3) {
      score[first] += 4 - choices[index];
    } else if (choices[index] >= 5 && choices[index] <= 7) {
      score[second] += choices[index] - 4;
    }
  });

  // 2. score 비교해서 성격 유형 검사 결과 만들기
  let answer = '';
  const characters = [
    ['R', 'T'],
    ['C', 'F'],
    ['J', 'M'],
    ['A', 'N'],
  ];

  characters.forEach((chars) => {
    const [char1, char2] = chars;

    if (score[char1] >= score[char2]) {
      answer += char1;
    } else {
      answer += char2;
    }
  });

  return answer;
}
