/**
 * This function calculates how many years it will take for a starting amount
 * of money to reach a target amount of money given an annual interest rate. 
 * Returns the number of years required to reach target.
 * 
 * @param {number} start - Starting amount of money
 * @param {number} target - Target amount of money
 * @param {number} interest - Interest rate
 * @returns {number} - Returns the count of years needed to reach target
 */
function savingsCalculator (start, target, interest) {
  let years = 0;
  while (start <= target) {
    start = start + Math.round(start * (interest / 100) * 1e2) / 1e2;
    years++;
  }
  return years;
}