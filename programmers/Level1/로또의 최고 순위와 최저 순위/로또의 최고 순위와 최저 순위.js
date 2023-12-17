function solution(lottos, win_nums) {
  let answer = [];
  let count = 0;
  let zeroCount = 0;
  const ranking = {
    6: 1,
    5: 2,
    4: 3,
    3: 4,
    2: 5,
    1: 6,
    0: 6,
  };

  for (let i = 0; i < 6; i++) {
    if ((lottos[i], win_nums.includes(lottos[i]))) {
      count += 1;
    }

    if (lottos[i] === 0) {
      zeroCount += 1;
    }
  }

  answer = [ranking[count + zeroCount], ranking[count]];
  return answer;
}
