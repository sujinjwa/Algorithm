// 문제 링크
// https://school.programmers.co.kr/learn/courses/30/lessons/81301

function solution(s) {
  let dict = {
    zero: '0',
    one: '1',
    two: '2',
    three: '3',
    four: '4',
    five: '5',
    six: '6',
    seven: '7',
    eight: '8',
    nine: '9',
  };
  let answer = '';
  let tmp = '';

  [...s].forEach((elem) => {
    tmp += elem;

    // 조회한 자릿수가 숫자인 경우 그대로 answer에 추가
    if (Number.isInteger(Number(tmp))) {
      answer += tmp;
      tmp = '';
    }

    // 조회한 자릿수가 정수인 경우 숫자를 나타내는 영단어인지 확인 후
    // 알맞은 숫자로 변환하여 answer에 추가
    if (tmp in dict) {
      answer += dict[tmp];
      tmp = '';
    }
  });

  return Number(answer);
}
