from flask import Flask, request, jsonify, render_template
import re

app = Flask(__name__)

def check_password_strength(password):
    length = len(password)
    character_set_size = 0

    if re.search(r"[a-z]", password):
        character_set_size += 26
    if re.search(r"[A-Z]", password):
        character_set_size += 26
    if re.search(r"[0-9]", password):
        character_set_size += 10
    if re.search(r"[_@$]", password):
        character_set_size += 33

    total_combinations = character_set_size ** length
    attempts_per_second = 1e9  # 1 billion attempts per second
    time_to_crack_seconds = total_combinations / attempts_per_second

    if len(password) < 8:
        return "Password too short", False, time_to_crack_seconds
    if not re.search(r"[a-z]", password):
        return "Password must contain at least one lowercase letter", False, time_to_crack_seconds
    if not re.search(r"[A-Z]", password):
        return "Password must contain at least one uppercase letter", False, time_to_crack_seconds
    if not re.search(r"[0-9]", password):
        return "Password must contain at least one number", False, time_to_crack_seconds
    if not re.search(r"[_@$]", password):
        return "Password must contain at least one special character", False, time_to_crack_seconds
    if re.search(r"\s", password):
        return "Password must not contain spaces", False, time_to_crack_seconds
    
    return "Strong password", True, time_to_crack_seconds

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_password', methods=['POST'])
def check_password():
    data = request.get_json()
    password = data.get('password')
    message, is_strong, crack_time = check_password_strength(password)
    return jsonify({"message": message, "is_strong": is_strong, "crack_time_seconds": crack_time})

if __name__ == '__main__':
    app.run(debug=True)
