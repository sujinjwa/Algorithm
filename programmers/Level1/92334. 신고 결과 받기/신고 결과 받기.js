function solution(id_list, report, k) {
  // 1. 각 유저별 경고 받은 횟수 저장
  const count = {};
  id_list.forEach((id) => (count[id] = 0));

  report = new Set(report);

  report.forEach((elem) => {
    const [id1, id2] = elem.split(' ');

    count[id2] += 1;
  });

  // 2. k번 이상 경고받은 유저는 이용 정지
  let wrongUsers = [];
  Object.entries(count).forEach(([id, cnt]) => {
    if (cnt >= k) {
      wrongUsers.push(id);
    }
  });

  // 3. report 조회하면서 각 유저별 이용 정지된 유저 신고한 횟수 구하기
  const count2 = {};
  id_list.forEach((id) => (count2[id] = 0));

  report.forEach((elem) => {
    const [id1, id2] = elem.split(' ');

    if (wrongUsers.includes(id2)) {
      count2[id1] += 1;
    }
  });

  // 4. answer 구하기
  let answer = [];
  Object.entries(count2).forEach(([_, cnt]) => {
    answer.push(cnt);
  });

  return answer;
}
