# Password Strength Checker

A web application that checks the strength of a password and estimates the time it would take to crack it. Built with Python (Flask) for the back-end and HTML, CSS, and JavaScript for the front-end.

## Features

- Checks password strength based on length, character variety, and the presence of special characters.
- Estimates the time it would take to crack the password.
- Simple and intuitive web interface.

## Project Structure
password_checker/
├── app.py
├── static/
│ ├── styles.css
│ ├── script.js
│ └── index.html
└── templates/
└── index.html


## Requirements

- Python 3.x
- Flask

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/kuldip024/password_strength_checker.git
   cd password_strength_checker
2. **Create a virtual environment (optional but recommended):**

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install the required packages:**
   \`\`\`
     pip install flask
   \`\`\`

# Usage

**1.Run the Flask application:**
 \`\`\` python app.py \`\`\`

**2.Open your web browser and navigate to:**
  \`\`\` http://127.0.0.1:5000/ \`\`\`

**3.Enter a password to check its strength and see the estimated time to crack it.**

# Example

# How It Works
- **Password Submission**: The user enters a password in the provided input field.
- **Strength Evaluation**: The backend processes the password to check its strength based on 
predefined criteria.
- **Crack Time Calculation**: The application calculates the possible combinations based on the password length and character set, and then estimates the time required to crack the password.
- **Feedback**: The user receives feedback on the password's strength and the estimated time to crack it.

# Why Use This Application?
With increasing cyber threats, it is crucial to use strong and secure passwords. The Password Strength Checker not only evaluates the robustness of a password but also educates users on the importance of password complexity by providing real-time feedback and crack time estimates. This tool is perfect for individuals looking to enhance their online security and for organizations aiming to enforce strong password policies among their users.

# Technology Stack
- **Backend**: Python with Flask framework
- **Frontend**: HTML, CSS, and JavaScript
- **Regular Expressions**: Used for password validation and character checks


# Contributing
Contributions are welcome! Please create a pull request with detailed descriptions of the changes.

# License
This project is licensed under the MIT License. See the LICENSE file for details.

# Contact
If you have any questions, feel free to reach out to me at kuldipramavat93@gmail.com.
