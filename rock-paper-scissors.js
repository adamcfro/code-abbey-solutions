/**
 * This function takes in a set of arguments and determines the winner of a set
 * of rock, paper scissors games. 'R' stands for rock, 'P' for paper, and 'S'
 * for scissors. Rock beats scissors, scissors beat paper, paper beats rock.
 * 
 * @param  {...any} args - An undetermined number of strings
 * @returns {Number} - Returns 1 or 2 depending on the winner
 */
function rockPaperScissors (...args) {
  let playerWins = {'p1': 0, 'p2': 0};
  for (let i = 0; i < args.length; i++) {
    let games = args[i].toLowerCase().split('');
    if (!(games[0] === games[1])) {
      if (games[0] === 'r' && games[1] === 's' ||
        games[0] === 'p' && games[1] === 'r' || 
        games[0] === 's' && games[1] === 'p') {
          playerWins['p1'] += 1;
      } else {
        playerWins['p2'] += 1;
      }
    }
  }
  let winner = playerWins['p1'] > playerWins['p2'] ? 1 : 2;
  return winner;
}