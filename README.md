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

bash
Copy code
pip install flask

# Usage

**1.Run the Flask application:**
  python app.py

**2.Open your web browser and navigate to:**
  http://127.0.0.1:5000/

**3.Enter a password to check its strength and see the estimated time to crack it.**

# Example

# How It Works
The application uses regular expressions to evaluate the password's strength based on the following criteria:

Length of at least 8 characters.
Contains at least one lowercase letter.
Contains at least one uppercase letter.
Contains at least one digit.
Contains at least one special character (_@$).
Does not contain spaces.

It also calculates the estimated time to crack the password based on the character set size and password length, assuming an attacker can attempt 1 billion passwords per second.

# Contributing
Contributions are welcome! Please create a pull request with detailed descriptions of the changes.

# License
This project is licensed under the MIT License. See the LICENSE file for details.

# Contact
If you have any questions, feel free to reach out to me at kuldipramavat93@gmail.com.
