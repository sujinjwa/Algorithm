function solution(new_id) {
  let answer = '';
  let newId = Array.from(new_id);

  // 1단계. 모든 대문자 -> 소문자로 치환
  newId = newId.map((elem) => elem.toLowerCase());

  // 2단계. 소문자, 숫자, 빼기, 밑줄, 마침표 제외한 모든 문자 제거
  newId = newId.filter((elem) => {
    return (
      (elem >= 'a' && elem <= 'z') ||
      elem === '-' ||
      elem === '_' ||
      elem === '.' ||
      (elem >= '0' && elem <= '9')
    );
  });

  // 3단계. 마침표 2번 이상 연속된 부분 1개로 치환
  let temp = [];
  let i = 0;
  while (i < newId.length) {
    if (newId[i] !== '.') {
      temp.push(newId[i]);
      i += 1;
    } else {
      let j = 1;
      while (true) {
        if (newId[i] !== newId[i + j]) {
          break;
        }
        j += 1;
      }

      temp.push(newId[i]);

      if (i === i + j - 1) {
        i += 1;
      } else {
        i += j;
      }
    }
  }
  newId = temp;

  // 4단계. 처음이나 끝에 마침표 있으면 제거
  if (newId[0] === '.') {
    newId = newId.slice(1);
  }

  if (newId[newId.length - 1] === '.') {
    newId.pop();
  }

  // 5단계. 빈 문자열이면 a 대입
  if (newId.length === 0) {
    newId.push('a');
  }

  // 6단계. 길이가 16자 이상이면 15개 이후 문자 모두 제거
  if (newId.length >= 16) {
    newId = newId.splice(0, 15);
  }

  if (newId[newId.length - 1] === '.') {
    newId.pop();
  }

  // 7단계. 길이가 2자 이하라면, 마지막 문자를 길이 3될때까지 반복해서 추가
  if (newId.length <= 2) {
    while (newId.length < 3) {
      newId.push(newId[newId.length - 1]);
    }
  }

  answer = newId.join('');

  return answer;
}
