function solution(numbers, hand) {
  let answer = '';

  // 키패드 숫자의 위치
  const number_pos = {
    1: [0, 0],
    2: [0, 1],
    3: [0, 2],
    4: [1, 0],
    5: [1, 1],
    6: [1, 2],
    7: [2, 0],
    8: [2, 1],
    9: [2, 2],
    0: [3, 1],
  };

  // 처음 시작할 때 왼손과 오른손의 위치에 해당하는 x, y 값
  let left_x = 3;
  let left_y = 0;
  let right_x = 3;
  let right_y = 2;

  numbers.forEach((number) => {
    if (number === 1 || number === 4 || number === 7) {
      const [next_x, next_y] = number_pos[number];
      left_x = next_x;
      left_y = next_y;
      answer += 'L';
    }

    if (number === 3 || number === 6 || number === 9) {
      const [next_x, next_y] = number_pos[number];
      right_x = next_x;
      right_y = next_y;
      answer += 'R';
    }

    if (number === 2 || number === 5 || number === 8 || number === 0) {
      const [x, y] = number_pos[number];
      const disWithLeft = Math.abs(left_x - x) + Math.abs(left_y - y);
      const disWithRight = Math.abs(right_x - x) + Math.abs(right_y - y);

      if (disWithLeft > disWithRight) {
        right_x = x;
        right_y = y;
        answer += 'R';
      } else if (disWithLeft < disWithRight) {
        left_x = x;
        left_y = y;
        answer += 'L';
      } else {
        if (hand === 'left') {
          left_x = x;
          left_y = y;
          answer += 'L';
        } else {
          right_x = x;
          right_y = y;
          answer += 'R';
        }
      }
    }
  });

  return answer;
}
