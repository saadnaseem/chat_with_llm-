from flask import Flask, request, jsonify, send_from_directory, Response
import requests
import json
import os

app = Flask(__name__)

OLLAMA_API_URL = 'http://localhost:11434/api/generate'  # Adjust if your Ollama API is different
HISTORY_FILE = 'chat_history.json'

# Helper to load chat history from disk
def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'r') as f:
            return json.load(f)
    return []

# Helper to save chat history to disk
def save_history(history):
    with open(HISTORY_FILE, 'w') as f:
        json.dump(history, f)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    history = load_history()

    # Send to Ollama
    payload = {
        'model': 'llama3.2',  # Change to your model name if needed
        'prompt': user_message,
        'stream': True
    }
    
    def generate():
        try:
            with requests.post(OLLAMA_API_URL, json=payload, stream=True) as response:
                response.raise_for_status()
                buffer = ''
                for line in response.iter_lines():
                    if line:
                        try:
                            data = json.loads(line.decode('utf-8'))
                            chunk = data.get('response', '')
                            if chunk:
                                # Format chunk as Markdown (paragraphs)
                                chunk = chunk.replace('. ', '.\n\n')
                                buffer += chunk
                                yield f"data: {chunk}\n\n"
                        except Exception:
                            continue
                # Save to history after streaming is done
                history.append({'role': 'user', 'message': user_message})
                history.append({'role': 'llm', 'message': buffer.strip()})
                save_history(history)
        except Exception as e:
            yield f"data: [Error contacting Ollama: {e}]\n\n"

    return Response(generate(), mimetype='text/event-stream')

@app.route('/history', methods=['GET', 'POST'])
def history():
    if request.method == 'GET':
        return jsonify(load_history())
    elif request.method == 'POST':
        history = request.json.get('history', [])
        save_history(history)
        return jsonify({'status': 'saved'})

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('.', path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True) 