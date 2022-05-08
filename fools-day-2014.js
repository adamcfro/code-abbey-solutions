/**
 * This function takes in a variable amount of number parameters, multiplies
 * each number by itself, and adds it to a sum, returning the sum of each
 * number.
 * 
 * @param  {...any} args - A variable amount of number parameters
 * @returns {Number} - Returns a sum of all parameters multiplied by themselves
 */
function foolsDay (...args) {
  let sum = 0;
  for (let num of args) {
    sum += num * num;
  }
  return sum;
}