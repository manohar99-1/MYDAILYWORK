# MYDAILYWORK
## Artificial Intelligence Internship Program

---

## 📁 Projects Overview

| # | Project | Tech Used |
|---|---|---|
| 1 | Rule-Based Chatbot | Python, ipywidgets |
| 2 | Tic Tac Toe with Minimax AI | Python |
| 3 | AI Image Caption Generator | BLIP, Streamlit, ngrok |

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
```
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9
```
- Enter a number **(1–9)** to place **X**
- AI automatically places **O**
- Game ends on win or draw

---

### Concepts Used
- Python Lists & Functions
- Recursion
- Minimax Algorithm
- Game Logic Design
- Input Handling

---

### Future Improvements
- Add difficulty levels
- Add graphical interface (Tkinter / Pygame)
- Add score tracking
- Improve AI speed with Alpha-Beta pruning

---

### Learning Outcome
- Understanding of recursion
- Implementation of game logic
- AI decision-making in games
- Clean program structure

---

---

## Project 3: AI Image Caption Generator

### Project Overview
A Streamlit web app that uses the **BLIP (Bootstrapped Language-Image Pretraining)** model to automatically generate captions for uploaded images. Deployed publicly via **ngrok** directly from Google Colab.

---

### Features
- Upload any JPG/PNG image
- AI-generated natural language caption
- Clean and styled Streamlit UI
- Runs on GPU (if available) or CPU
- Publicly accessible via ngrok tunnel

---

### Technologies Used
- Python 3
- Hugging Face Transformers (BLIP model)
- Streamlit
- PyTorch
- Pillow
- pyngrok
- Google Colab

---

### How It Works
1. User uploads an image via the Streamlit interface
2. Image is processed by `BlipProcessor`
3. `BlipForConditionalGeneration` generates a caption
4. Caption is displayed in a styled green heading

---

### Model Used
| Detail | Info |
|---|---|
| Model | `Salesforce/blip-image-captioning-base` |
| Source | Hugging Face |
| Task | Image-to-text captioning |

---

### Concepts Demonstrated
- Pretrained vision-language models
- Streamlit web app development
- Model caching with `@st.cache_resource`
- Tunneling with ngrok from Colab
- GPU/CPU device handling

---

### Possible Improvements
- Deploy permanently on Hugging Face Spaces
- Support batch image captioning
- Add multilingual caption support
- Allow caption length control
- Add image preprocessing options

---

### Learning Outcome
- How vision-language models work
- Deploying ML models as web apps
- Using Hugging Face Transformers in practice
- Running and exposing Colab apps publicly

---

## 🛠️ General Tech Stack

| Tool | Purpose |
|---|---|
| Python 3 | Core language |
| ipywidgets | Interactive Jupyter UI |
| Hugging Face Transformers | Pretrained AI models |
| Streamlit | Web app framework |
| PyTorch | Deep learning backend |
| pyngrok | Public URL tunneling |
| Google Colab | Cloud notebook environment |

---

## 📚 Overall Learning Outcomes

- Building rule-based and AI-powered applications
- Implementing classic algorithms like Minimax
- Working with pretrained vision-language models
- Deploying ML apps as interactive web interfaces
- Hands-on experience with the full AI project lifecycle
