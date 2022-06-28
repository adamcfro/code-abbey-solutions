/**
 * This function seeks to simulate a pair of dice throws. It takes any amount 
 * of number pairs, then takes the modulo of each number plus one, adds the 
 * numbers together, and returns a string of the result of all dice throws.
 * 
 * @param  {...number} args - Any amount of numbers
 * @returns - Returns a string representation of dice throws
 */
function doubleDiceRoll (...args) {
  let returnValues = [];
  for (let i = 0; i < args.length; i += 2) {
    num1 = (args[i] % 6) + 1;
    num2 = (args[i + 1] % 6) + 1;
    returnValues.push(num1 + num2);
  }
  return returnValues.join(' ');
}