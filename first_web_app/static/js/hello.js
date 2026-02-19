const greetButton = document.getElementById('greet-button');
const welcomeMessage = document.getElementById('name-input');

greetButton.addEventListener('click', () => {
    const name = welcomeMessage.value;
    if (name.trim() === '' || name === null) {
        alert('Please enter your name!');
        return;
    }
    alert(`Hello, ${name}! Welcome to our website!`);
});

// DOM = Document Object Model
// Card (html, css)