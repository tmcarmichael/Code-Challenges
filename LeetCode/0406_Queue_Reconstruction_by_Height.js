/*
406. Queue Reconstruction by Height

https://leetcode.com/problems/queue-reconstruction-by-height/
*/

/**
 * @param {number[][]} people
 * @return {number[][]}
 */
var reconstructQueue = function (people) {
  people.sort((a, b) => {
    if (a[0] - b[0] > 0) return -1;
    else if (a[0] - b[0] < 0) return 1;
    else if (a[1] - b[1] > 0) return 1;
    else return -1;
  });
  let res = [];
  for (p of people) {
    res.splice(p[1], 0, p);
  }
  return res;
};
