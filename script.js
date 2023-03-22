const chatForm = document.querySelector('#chat-form');
const chatBox = document.querySelector('#chat-box');

chatForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const userInput = document.querySelector('#user-input').value.trim();
    if (userInput === '') {
        return;
    }
    const data = {
        user_input: userInput
    };
    const response = await fetch('/get_response', {
        method: 'POST',
        body: new URLSearchParams(data)
    });
    const json = await response.json();
    appendBotResponse(json.response);
    chatBox.scrollTop = chatBox.scrollHeight;
    chatForm.reset();
});

function appendBotResponse(response) {
    const responseElement = document.createElement('div');
    responseElement.classList.add('bot-response');
    responseElement.innerHTML = `<span class="bot-bubble">${response}</span>`;
    chatBox.appendChild(responseElement);
}
