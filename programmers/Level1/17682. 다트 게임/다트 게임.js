function solution(dartResult) {
  let answer = 0;
  let temp = [[], [], []]; // 3^3 공간 필요
  let temp_index = 0;

  const dartArray = Array.from(dartResult);

  const push_temp = (index, number, bonus, option) => {
    if (bonus === 'D') {
      number *= number;
    } else if (bonus === 'T') {
      number = number * number * number;
    }

    temp[index].push(number);

    if (option === '*') {
      temp[index].push(2);
      if (index > 0) {
        temp[index - 1].push(2);
      }
    } else if (option === '#') {
      temp[index].push(-1);
    }
  };

  let index = 0;
  while (index < dartArray.length) {
    if (!Number.isNaN(Number(dartArray[index]))) {
      if (!Number.isNaN(Number(dartArray[index + 1]))) {
        const bonus = dartArray[index + 2];
        const option = dartArray[index + 3];

        push_temp(temp_index, 10, bonus, option);

        index += 2;
      } else {
        const bonus = dartArray[index + 1];
        const option = dartArray[index + 2];

        push_temp(temp_index, Number(dartArray[index]), bonus, option);

        index += 1;
      }
      temp_index += 1;
    }
    index += 1;
  }

  for (const array of temp) {
    let score = 1;
    array.forEach((elem) => (score *= elem));

    answer += score;
  }

  return answer;
}
