/**
 * This function takes an input string and counts how many times each word
 * in the string is used. Words used more than once are alphabetized and 
 * returned in an array in sorted order.
 * 
 * @param {String} str - A string parameter
 * @returns {Array} - Returns an array of sorted strings
 */
function matchingWords (str) {
  let repeats = {};
  let magicalPhrase = [];
  let splitWords = str.split(' ').sort();
  for (let elem of splitWords) {
    repeats[elem] = (repeats[elem] || 0) + 1;
  }
  for (let [key, value] of Object.entries(repeats)) {
    if (value > 1) {
      magicalPhrase.push(key);
    }
  }
  return magicalPhrase;
}