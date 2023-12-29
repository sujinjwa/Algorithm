function solution(board, moves) {
  let answer = 0;
  let temp_array = [];

  // 1. board에서 moves에 해당하는 column의 맨 윗상단 row에 위치하는 인형 구한다
  // 1-1. 해당 위치는 0으로 바꿔준다
  // 2. 그 인형을 temp_array에 넣어준다
  // 3. 이때 temp_array[-1] 와 동일한 인형이면 둘 다 터뜨리고 answer + 2 해준다

  const pushTemp = (number) => {
    if (temp_array.length > 0 && temp_array[temp_array.length - 1] === number) {
      temp_array.pop();
      answer += 2;
    } else {
      temp_array.push(number);
    }
  };

  for (const move of moves) {
    for (let i = 0; i < board.length; i++) {
      if (board[i][move - 1]) {
        pushTemp(board[i][move - 1]);
        board[i][move - 1] = 0;
        break;
      }
    }
  }

  return answer;
}
