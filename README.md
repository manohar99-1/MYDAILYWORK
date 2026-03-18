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
