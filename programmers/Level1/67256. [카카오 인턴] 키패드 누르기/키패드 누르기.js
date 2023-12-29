function solution(numbers, hand) {
  let answer = '';

  // numbers 조회하면서 왼손과 오른손 각각 위치 이동시키기
  // numbers 조회하면서, 1,4,7 - 왼손, 3,6,9 - 오른손, 2,5,8 - 왼손 & 오른손 위치 구해서 더 가까운 손이 위치 이동

  let left = [3, 0];
  let right = [3, 2];

  numbers.forEach((number) => {
    if (number === 1) {
      left = [0, 0];
      answer += 'L';
    }

    if (number === 4) {
      left = [1, 0];
      answer += 'L';
    }

    if (number === 7) {
      left = [2, 0];
      answer += 'L';
    }

    if (number === 3) {
      right = [0, 2];
      answer += 'R';
    }

    if (number === 6) {
      right = [1, 2];
      answer += 'R';
    }

    if (number === 9) {
      right = [2, 2];
      answer += 'R';
    }

    if (number === 2) {
      // [0, 1]
      const left_dis = Math.abs(left[0] - 0) + Math.abs(left[1] - 1);
      const right_dis = Math.abs(right[0] - 0) + Math.abs(right[1] - 1);

      if (left_dis > right_dis) {
        right = [0, 1];
        answer += 'R';
      } else if (left_dis < right_dis) {
        left = [0, 1];
        answer += 'L';
      } else {
        if (hand === 'left') {
          left = [0, 1];
          answer += 'L';
        } else {
          right = [0, 1];
          answer += 'R';
        }
      }
    }

    if (number === 5) {
      // left = [1, 0] // 4, // 5 = [1, 1], right = [0, 2]
      const left_dis = Math.abs(left[0] - 1) + Math.abs(left[1] - 1);
      const right_dis = Math.abs(right[0] - 1) + Math.abs(right[1] - 1);

      if (left_dis > right_dis) {
        right = [1, 1];
        answer += 'R';
      } else if (left_dis < right_dis) {
        left = [1, 1];
        answer += 'L';
      } else {
        if (hand === 'left') {
          left = [1, 1];
          answer += 'L';
        } else {
          right = [1, 1];
          answer += 'R';
        }
      }
    }

    if (number === 8) {
      const left_dis = Math.abs(left[0] - 2) + Math.abs(left[1] - 1);
      const right_dis = Math.abs(right[0] - 2) + Math.abs(right[1] - 1);

      if (left_dis > right_dis) {
        right = [2, 1];
        answer += 'R';
      } else if (left_dis < right_dis) {
        left = [2, 1];
        answer += 'L';
      } else {
        if (hand === 'left') {
          left = [2, 1];
          answer += 'L';
        } else {
          right = [2, 1];
          answer += 'R';
        }
      }
    }

    if (number === 0) {
      const left_dis = Math.abs(left[0] - 3) + Math.abs(left[1] - 1);
      const right_dis = Math.abs(right[0] - 3) + Math.abs(right[1] - 1);

      if (left_dis > right_dis) {
        right = [3, 1];
        answer += 'R';
      } else if (left_dis < right_dis) {
        left = [3, 1];
        answer += 'L';
      } else {
        if (hand === 'left') {
          left = [3, 1];
          answer += 'L';
        } else {
          right = [3, 1];
          answer += 'R';
        }
      }
    }
  });

  return answer;
}
