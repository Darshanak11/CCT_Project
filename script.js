async function play(userChoice) {
    try {
        const response = await fetch('/play', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ choice: userChoice })
        });
        const data = await response.json();
        document.getElementById('result').textContent =
            `You ${data.result}! Computer choice :  ${data.computer_choice}.`;
    } catch (error) {
        console.error('Error connecting to the server:', error);
        document.getElementById('result').textContent = 
            "Error: Couldn't connect to the server.";
    }
}
