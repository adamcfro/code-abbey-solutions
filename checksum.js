/**
 * Returns a sum, calculated as follows:
 * for each element of the array, add this element to the sum variable and 
 * multiply this sum by 113, then use modulo 10000007 on this result.
 * 
 * @param {Array} arr - An array of numbers
 * @returns {Number} - Returns a sum
 */
function checksum (arr) {
  let sum = 0;
  for (val of arr) {
    sum = (sum + val) * 113 % 10000007;
  }
  return sum;
}