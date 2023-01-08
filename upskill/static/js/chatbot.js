

const API_KEY = {{api_key}};
const MODEL = "text-davinci-002";

// Function to send a message to the chatbot and receive a response
async function getResponse(message) {
  const response = await fetch(`https://api.openai.com/v1/completions`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Authorization": `Bearer ${API_KEY}`
    },
    body: JSON.stringify({
      prompt: message,
      model: MODEL,
      max_tokens: 1024
    })
  });
  const responseJson = await response.json();
  return responseJson.choices[0].text;
}

// Function to add a message to the chatbot interface
function addMessage(message, sender) {
  const messagesDiv = document.getElementById("chatbot-messages");
  const messageDiv = document.createElement("div");
  messageDiv.classList.add("message");
  if (sender === "user") {
    messageDiv.classList.add("user-message");
  } else {
    messageDiv.classList.add("chatbot-message");
  }
  messageDiv.innerText = message;
  messagesDiv.appendChild(messageDiv);
  messagesDiv.scrollTop = messagesDiv.scrollHeight;
}

// Handle form submission to send a message to the chatbot
const form = document.getElementById("chatbot-form");
form.addEventListener("submit", event => {
  event.preventDefault();
  const input = document.getElementById("chatbot-input");
  const message = input.value;
  input.value = "";
  addMessage(message, "user");
  getResponse(message).then(response => {
    addMessage(response, "chatbot");
  });
});
