document.getElementById('passwordForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const password = document.getElementById('password').value;
    
    fetch('/check_password', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ password: password })
    })
    .then(response => response.json())
    .then(data => {
        const resultDiv = document.getElementById('result');
        const timeToCrack = data.crack_time_seconds;
        let timeToCrackText = '';

        if (timeToCrack < 60) {
            timeToCrackText = `${timeToCrack.toFixed(2)} seconds`;
        } else if (timeToCrack < 3600) {
            timeToCrackText = `${(timeToCrack / 60).toFixed(2)} minutes`;
        } else if (timeToCrack < 86400) {
            timeToCrackText = `${(timeToCrack / 3600).toFixed(2)} hours`;
        } else if (timeToCrack < 31536000) {
            timeToCrackText = `${(timeToCrack / 86400).toFixed(2)} days`;
        } else {
            timeToCrackText = `${(timeToCrack / 31536000).toFixed(2)} years`;
        }

        resultDiv.textContent = `${data.message}. Estimated time to crack: ${timeToCrackText}`;
        resultDiv.style.color = data.is_strong ? 'green' : 'red';
    })
    .catch(error => console.error('Error:', error));
});
