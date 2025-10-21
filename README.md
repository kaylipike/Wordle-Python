# 5-Letter Wordle
**5-Letter Wordle** demonstrates proficiency in Python programming, problem-solving, collaboration, and the ability to extend class-learned concepts into a fully functional, interactive project.

## Project Overview

This is a Python-based implementation of the popular word-guessing game *Wordle*. In this game, the program randomly selects a 5-letter secret word from a predefined word list. Players have 10 attempts to guess the secret word, receiving feedback after each guess in the form of color-coded letters:

- **Green**: Correct letter in the correct position  
- **Yellow**: Correct letter in the wrong position  
- **Red**: Letter not in the secret word  

The game ensures that guesses are valid 5-letter words from the list and prevents duplicate guesses. It also correctly handles duplicate letters, ensuring accurate color feedback based on the number of occurrences in the secret word.

## Key Features

- **Random Word Selection:** Secret word chosen randomly from a supplied 5-letter word list.
- **Input Validation:** Ensures user input is a valid 5-letter word, contains only letters, is in the word list, and has not been guessed before.
- **Duplicate Letter Handling:** Correctly colors repeated letters in user guesses according to their frequency in the secret word.
- **Replayable:** Users are prompted to play again after each game.
- **PEP 8 Compliance:** Code adheres approximately to Python’s PEP 8 standards using `flake8`.
- **Color Feedback:** Utilizes `colorama` to provide colored feedback in the terminal for an interactive experience.

## Technologies & Libraries

- Python
- [`colorama`](https://pypi.org/project/colorama/) – for colored terminal output
- [`collections.Counter`](https://docs.python.org/3/library/collections.html#collections.Counter) – for handling letter frequencies
- [`re`](https://docs.python.org/3/library/re.html) – for validating input
- [`random`](https://docs.python.org/3/library/random.html) – for selecting the secret word

## Collaboration & Learning

This project was a collaborative effort:

- Kayli Pike: Implemented input validation, file reading, identified a reliable 5-letter word list, and worked on how to handle duplicate letters in a word.
- Jackie Littlefield: Led the main game loop implementation, including feedback color logic, with contributions from Kayli.
- Together: Refactored code into functions, ensured PEP 8 compliance, and tested all functionalities including edge cases.

## Testing & Validation

The program was rigorously tested to ensure:

- Correct color feedback for all guess scenarios, including duplicate letters.
- Accurate validation for word length, allowed characters, and word list membership.
- Prevention of repeated guesses.
- Proper termination and replay functionality.

## Next Steps / Future Improvements

- Implement a graphical user interface for a more user-friendly experience.
- Refine the word list for greater challenge and variety.
- Provide clearer instructions at the start of the game.
- Include additional statistics, such as average number of guesses to solve a word.

## References

- [Regex in Python](https://www3.ntu.edu.sg/home/ehchua/programming/howto/Regexe.html)  
- [List of 5-Letter Words](https://copylists.com/words/list-of-5-letter-words/)  
- [Python `collections.Counter`](https://chercher.tech/python/how-to-use-collections-counter-in-python)

---

## Contact

For questions, feedback, or collaboration inquiries, please contact:

**Email:** [kayli.pike@gmail.com](mailto:kayli.pike@gmail.com)

---

**© 2023 Kayli Pike**

