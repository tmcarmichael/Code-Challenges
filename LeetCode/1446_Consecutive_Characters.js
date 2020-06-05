/*
1446. Consecutive Characters

Q: https://leetcode.com/problems/consecutive-characters/
*/

/**
 * @param {string}
 * @return {number}
 */
var maxPower = function (s) {
  let current = '';
  let maxV = 1;
  for (char of s) {
    if (char != current) {
      current = char;
      currentPower = 1;
    } else {
      currentPower += 1;
      maxV = maxV > currentPower ? maxV : currentPower;
    }
  }
  return maxV;
};
