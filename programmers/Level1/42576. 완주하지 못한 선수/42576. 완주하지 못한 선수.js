function solution(participant, completion) {
  var answer = '';
  let completePeople = {};

  // participant: 마라톤에 참여한 선수들의 이름들
  // completion: 마라톤 완주한 선수들의 이름들

  // 1. 완주한 선수들 돌면서, 해당 이름을 key로 하는 객체 만들기
  completion.forEach((person) => {
    if (completePeople[person]) {
      completePeople[person] += 1;
    } else {
      completePeople[person] = 1;
    }
  });

  // 2. 참여한 선수들 돌면서, 완주한 선수들 객체에 없으면 그 사람이 정답!
  participant.forEach((person) => {
    if (!completePeople[person] || completePeople[person] === 0) {
      answer = person;
    } else {
      completePeople[person] -= 1;
    }
  });

  return answer;
}
