/**
 * This function checks whether brackets in a string are in the correct order.
 * 
 * @param {String} str - A string parameter containing a variety of brackets
 * @returns {Boolean} - Returns true if the brackets are in order
 */
function matchingBrackets (str) {
  let left = ['(', '[', '{', '<'];
  let right = [')', ']', '}', '>'];
  let brackets = [];
  for (let i = 0; i < str.length; i++) {
    if (left.includes(str[i])) {
      brackets.push(str[i]);
    } else if (right.includes(str[i])) {
      let index = right.indexOf(str[i]);
      if (brackets[brackets.length - 1] === left[index]) {
        brackets.pop();
      }
    }
  }
  return brackets.length === 0;
}