# MYDAILYWORK
# Artificial Intelligence Internship Program ( MYDAILYWORK )

---

## Project 1: Rule-Based Chatbot

### Project Overview
A simple rule-based chatbot built using Python and `ipywidgets`. The chatbot responds to predefined user inputs such as greetings, time, date, jokes, and help commands using conditional logic. No machine learning involved.

---

### Features
- Interactive UI using `ipywidgets`
- Rule-based text processing
- Greeting detection (hello, hi, hey)
- Time and date response
- Joke generator
- Basic help menu
- Exit/disable chat functionality
- Chat history display

---

### Technologies Used
- Python 3
- ipywidgets
- datetime module

---

### How It Works
1. The user types a message
2. Input is converted to lowercase
3. Keywords are matched using conditional statements
4. A predefined response is returned on match
5. A fallback message is shown if no match is found

---

### Supported Commands
| Command | Response |
|---|---|
| hello / hi / hey | Greeting |
| how are you | Status reply |
| your name | Bot introduction |
| time | Current time |
| date | Current date |
| joke | Random joke |
| weather | Weather info |
| help | Help menu |
| bye / exit | Disables chat |

---

### Concepts Demonstrated
- Conditional statements
- String handling & keyword matching
- Event-driven programming
- Basic GUI with ipywidgets
- User interaction design

---

### Possible Improvements
- Add more conversation patterns
- Integrate NLP
- Connect to live APIs (weather, news)
- Add chatbot personality modes
- Convert to web app using Flask or Streamlit
- Implement ML-based chatbot

---

### Learning Outcome
- How chatbots work at a basic level
- User input handling
- Building interactive UI in Jupyter
- Structuring rule-based systems

---
---

## Project 2: Tic Tac Toe with Minimax AI

### Project Overview
A command-line Tic Tac Toe game built using Python where the player competes against an unbeatable AI powered by the **Minimax algorithm**. No external libraries required.

---

### Features
- Human vs AI gameplay
- Unbeatable AI using Minimax algorithm
- Winner & draw detection
- Input validation
- Replay option

---

### How the AI Works
The AI uses the **Minimax algorithm** — a recursive decision-making algorithm for turn-based games.

- AI **(O)** → maximizes score
- Player **(X)** → minimizes score
- All possible future moves are evaluated
- AI always picks the optimal move

Result: The AI **never loses** — it always forces a win or draw.

---

### Game Board Layout
