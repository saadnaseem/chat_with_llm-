# Local Chat with LLM (Ollama + Flask)

![My Diagram](images_github.png)

A simple web chat interface to interact with a local LLM (via [Ollama](https://ollama.com/)) using a modern HTML frontend and a Python Flask backend.

---

## Features

- Clean chat interface (like ChatGPT)
- Messages sent to your local Ollama LLM
- Real-time streaming responses: LLM replies appear word-by-word as they are generated
- Chat history saved to disk and downloadable as JSON
- Responses are formatted with Markdown for improved readability (paragraphs, bullet points, bold, etc.)

---

## Requirements

- Python 3.7+
- [Ollama](https://ollama.com/) running locally

---

## Installation

1. **Clone this repository:**
   ```bash
   git clone https://github.com/yourusername/chat_with_model.git
   cd chat_with_model
   ```

2. **Install Python dependencies:**
   ```bash
   pip install flask requests
   ```

3. **Install and start Ollama:**
   - [Download and install Ollama](https://ollama.com/download)
   - Start Ollama in a separate terminal:
     ```bash
     ollama serve
     ```
   - (Optional) Pull a model, e.g.:
     ```bash
     ollama pull llama2
     ```

---

## Usage

1. **Start the Flask server:**
   ```bash
   python chat_with_model/server.py
   ```

2. **Open your browser and go to:**
   ```
   http://localhost:5000
   ```

3. **Chat with your LLM!**
   - Type messages and press Send.
   - LLM responses will appear in real time, streaming word-by-word.
   - Output is formatted using Markdown for easy reading (paragraphs, bullet points, etc.).
   - Download chat history with the button in the top right.

---

## Notes

- By default, the backend uses the `llama2` model. Change the model name in `server.py` if you want to use another.
- Chat history is saved in `chat_history.json` in the project folder.
- Do **not** share your `chat_history.json` if you want to keep your chats private.

---

## License

MIT License 
