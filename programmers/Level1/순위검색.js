function solution(info, query) {
  // info(문자열): '개발언어 직군 경력 소울푸드 점수'
  // query(문자열 담긴 배열): ['개발팀의 문의1', '문의2', ...]
  // 문의 형식: '개발언어 and 직군 and 경력 and 소울푸드 점수'
  // '-' 표시는 조건 고려하지 않겠다는 의미
  // ex) 'cpp and - and senior and - 500'

  let applicants = [];
  info.forEach((applicant) => {
    let array = applicant.split(' ');
    applicants.push(array);
  });

  // answer(배열): 각 문의조건에 해당하는 사람들의 숫자로 이루어진 배열
  var answer = [];

  let queries = [];
  query.forEach((ques) => {
    let array = ques.split(' and ');
    let array2 = array[3].split(' ');
    array = array.slice(0, 3);
    array2.forEach((elem) => array.push(elem));

    queries.push(array);
  });

  for (let i = 0; i < queries.length; i++) {
    let cnt = 0;
    for (let j = 0; j < applicants.length; j++) {
      for (let k = 0; k < 4; k++) {
        if (parseInt(queries[i][4]) > parseInt(applicants[j][4])) break;

        if (queries[i][k] !== '-' && queries[i][k] !== applicants[j][k]) {
          break;
        }

        if (k === 3) {
          cnt += 1;
        }
      }
    }

    answer.push(cnt);
  }

  return answer;
}
