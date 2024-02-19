function solution(sizes) {
  let max_w = 0;
  let max_h = 0;
  sizes.forEach(([w, h]) => {
    if (w >= h) {
      max_w = Math.max(max_w, w);
      max_h = Math.max(max_h, h);
    } else {
      max_w = Math.max(max_w, h);
      max_h = Math.max(max_h, w);
    }
  });

  return max_w * max_h;
}
