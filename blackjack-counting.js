/**
 * This function adds up the cards from a blackjack hand and returns the total
 * if the total is less than 21, otherwise returns 'Bust'.
 * 
 * @param  {...any} args - A variable number of numbers and string characters
 * @returns {Number/String} - Returns a number if total is less than 21, else
 * returns the string 'Bust'. 
 */
function blackjackCounting (...args) {
  let total = 0;
  let cards = ['T', 'J', 'Q', 'K'];
  for (let card of args) {
    if (card === 'A') {
      total += total <= 10 ? 11 : 1;
    } else if (cards.includes(card)) {
      total += 10;
    } else {
      total += card;
    }
  }
  return total <= 21 ? total : 'Bust';
}