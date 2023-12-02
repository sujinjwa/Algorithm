function solution(name, yearning, photo) {
  // 사진 별로 추억 점수 매기려고 한다
  // 사진 속에 나오는 인물의 그리움 점수 합산 값 = 사진의 추억 점수

  // 1. name이랑 yearning을 순회하면서 사람 별 그리움 점수 나타내는 dict 만든다
  let dict = {};
  // for(let i=0; i<name.length; i++) {
  //     dict[name[i]] = yearning[i];
  // }
  name.forEach((n, i) => (dict[n] = yearning[i]));

  // 2. photo를 순회하면서 추억 점수 계산 및 result에 추가
  let answer = [];
  // for(let i=0; i<photo.length; i++) {
  //     let score = 0;
  //     for(let j=0; j<photo[i].length; j++) {
  //         if(photo[i][j] in dict)
  //             score += dict[photo[i][j]];
  //     }
  //     answer.push(score);
  // }

  photo.forEach((p) => {
    let score = 0;
    p.forEach((person) => {
      if (person in dict) score += dict[person];
    });
    answer.push(score);
  });

  return answer;
}
