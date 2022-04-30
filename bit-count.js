/**
 * This function takes in a number as a parameter, then uses a helper function
 * to convert the number to a binary string. It then returns a count of the
 * number of 1's in the binary string.
 * 
 * @param {Number} n - A number to convert to binary
 * @returns {Number} - Returns a count of the number of 1's in a binary string
 */
function bitCount (n) {
  let binaryStr = toBinary(n);
  let count = 0;
  for (let i = 0; i < binaryStr.length; i++) {
    if (binaryStr[i] === '1') {
      count++;
    }
  }
  return count;
}

/**
 * This function converts a number to a binary string.
 * 
 * @param {Number} num - A number parameter
 * @returns {String} - Returns a binary string
 */
function toBinary (num) {
  if (num === 1) {
    return '1';
  }
  if (num === 0) {
    return '0';
  }
  return toBinary(Math.floor(num / 2)) + (num % 2);
}