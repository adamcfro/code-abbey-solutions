/**
 * This function creates a representation of cards using a series of input
 * numbers to assign a suit and rank to any of 52 cards.
 * Returns a string representation of a hand of cards.
 * 
 * @param  {...any} args - An variable amount of numbers
 * @returns {String} - Returns a string representation of a hand of cards
 */
function cardNames (...args) {
  let cardsInHand = '';
  let suits = ['Clubs', 'Spades', 'Diamonds', 'Hearts'];
  let ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace'];
  for (let i = 0; i < arguments.length; i++) {
    let suitValue = suits[Math.floor(args[i] / 13)];
    let rankValue = ranks[args[i] % 13];
    cardsInHand += `${rankValue}-of-${suitValue}`;
    if (i !== arguments.length - 1) {
      cardsInHand += ' ';
    }
  }
  return cardsInHand;
}