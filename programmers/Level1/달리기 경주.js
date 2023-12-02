// Level 1. 달리기 경주 게임
// https://school.programmers.co.kr/learn/courses/30/lessons/178871?language=javascript

function solution(players, callings) {
  // 달리기 경주
  // 바로 앞의 선수 추월할 때 추월한 선수 이름 부른다
  // 1등부터 현재 등수 순서대로 담긴 문자열 배열 players
  // 경주 끝났을 때 선수들의 이름을 1등부터 등수 순서대로 배열 담아 return

  let ranks = {};
  players.forEach((player, i) => (ranks[player] = i));

  callings.forEach((player) => {
    let front_player = players[ranks[player] - 1];
    ranks[player] -= 1;
    ranks[front_player] += 1;

    players[ranks[player]] = player;
    players[ranks[front_player]] = front_player;
    // O(N)의 시간 걸리는 아래의 for문 대신 위의 hash 사용
    // for (const [key, value] of Object.entries(ranks)) {
    //     if(key !== player && value === ranks[player])
    //         ranks[key] += 1;
    // }
  });

  let answer = [];
  players.forEach((r) => answer.push(''));
  for (const [key, value] of Object.entries(ranks)) {
    answer[value] = key;
  }

  return answer;
}
