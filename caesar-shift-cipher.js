/**
 * Shifts an encryped Caesar cipher back to decode it.
 * Takes in a numeric value to shift the str parameter to the left by,
 * wrapping around for any ascii value below 65.
 * 
 * @param {Number} shift - A number to shift the cipher by
 * @param {String} str - A string parameter
 * @returns {String} - Returns a decoded string
 */
function caesarShiftCipher (shift, str) {
  let message = '';
  for (let i = 0; i < str.length; i++) {
    if (str.charCodeAt(i) < 65 || str.charCodeAt(i) > 90) {
      message += str[i];
    } else {
      let asciiChar = str.charCodeAt(i) - shift;
      if (asciiChar < 65) {
        message += String.fromCharCode(asciiChar + 26);
      } else {
        message += String.fromCharCode(asciiChar);
      }
    }
  }
  return message;
}