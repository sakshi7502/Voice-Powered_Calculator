// Function to handle typed input calculation
function calculate() {
    var expression = document.getElementById('expression').value;
    
    fetch('/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ expression: expression }),
    })
    .then(response => response.text())
    .then(data => {
        document.getElementById('result').innerText = 'Result: ' + data;
        document.getElementById('error').innerText = ''; // Clear error message
    })
    .catch(error => {
        document.getElementById('error').innerText = 'Error: ' + error;
    });
}

// Function to handle voice input calculation
function voiceCalculate() {
    fetch('/voice-calculate', {
        method: 'POST'
    })
    .then(response => response.text())
    .then(data => {
        document.getElementById('result').innerText = 'Result: ' + data;
        document.getElementById('error').innerText = ''; // Clear error message
    })
    .catch(error => {
        document.getElementById('error').innerText = 'Error: ' + error;
    });
}
