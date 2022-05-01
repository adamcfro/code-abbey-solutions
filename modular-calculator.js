/**
 * This function performs a series of operations sequentially, starting
 * with the parameter number, returning the result taken by modulo.
 * 
 * @param {Number} num - A number parameter
 * @returns {Number} - Returns a number
 */
function modularCalculator (num) {
  result = (((num + 3) * 7) + 10) * 2 * 3 + 1;
  return result % 11;
}