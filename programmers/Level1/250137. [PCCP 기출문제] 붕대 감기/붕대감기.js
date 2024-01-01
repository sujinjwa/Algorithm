function solution(bandage, health, attacks) {
  let answer = 0;

  const [healthTime, healthAmount, healthPlus] = bandage;
  const lastTime = attacks[attacks.length - 1][0];

  const maxHealth = health;
  let currentHealth = health;
  let consistent = 0;

  for (let currentTime = 1; currentTime <= lastTime; currentTime++) {
    // currentHealth가 0 이하가 되면 죽음 break
    if (currentHealth <= 0) {
      break;
    }

    // 몬스터 공격 받기
    const [attackTime, attackAmount] = attacks[0];
    if (attackTime === currentTime) {
      currentHealth -= attackAmount;
      attacks = attacks.slice(1);
      consistent = 0;
      continue;
    }

    // 체력 충전
    currentHealth += healthAmount;

    if (currentHealth > maxHealth) {
      currentHealth = maxHealth;
    }
    consistent += 1;

    // 추가 체력 충전
    if (consistent === healthTime) {
      currentHealth += healthPlus;
      if (currentHealth > maxHealth) {
        currentHealth = maxHealth;
      }
      consistent = 0;
    }
  }

  answer = currentHealth;

  if (answer <= 0) {
    return -1;
  }

  return answer;
}
