
# Slot Machine Game

This is a simple slot machine game developed in Python, using the random library for generating random numbers.

## How to Play

To play the game, run the `main.py` script in your Python environment.

At the beginning of the game, you will be prompted to enter the amount you want to deposit into your wallet. This amount will be used to place bets and play the game.

Once you have deposited the desired amount, the game will start. You will see three reels, each displaying a 3x3 matrix arrangement of random alphabets (A, B, C, and D). To win, you need to get three matching symbols in a row horizontally on the number of lines you have bet on (1-3).

At the start of each turn, you will be prompted to enter the number of lines you want to bet on (1-3). The more lines you bet on, the higher your chances of winning, but the higher the bet amount as well. You will then be prompted to enter the bet amount for each line.

You start with the amount you deposited into your wallet. Each spin costs the total bet amount, which is the number of lines multiplied by the bet amount. If you win, you earn the corresponding payout amount, which depends on the number of lines and the winning symbol. If you lose, you lose the bet amount.

To spin the reels, simply press the enter key.

Enjoy playing the game!

## Requirements

This game was developed using Python 3.8.5 and the following libraries:

- random

## Installation

1. Clone the repository using Git:

   ```bash
   git clone https://github.com/SHIYADBAVA/SlotMachine.git
   ```

2. Open the project in your preferred IDE. We recommend using VScode.

3. Run the `main.py` script.

## Contribution

Contributions are welcome! If you find a bug or have an idea for a new feature, please create a pull request or submit an issue.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
