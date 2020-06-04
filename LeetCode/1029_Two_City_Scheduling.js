/*
1029. Two City Scheduling

Q: https://leetcode.com/problems/two-city-scheduling/
*/

/**
 * @param {number[][]} costs
 * @return {number}
 */
function compareHelper(a, b) {
  if (a[1] - a[0] >= b[1] - b[0]) return 1;
  return -1;
}

function twoCitySchedCost(costs) {
  let res = 0;
  let len = costs.length;
  costs.sort(compareHelper);
  for (let i = 0; i < len; ++i) {
    if (i < len / 2) res += costs[i][1];
    else res += costs[i][0];
  }
  return res;
}
