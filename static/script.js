function sendMessage() {
  const message = document.getElementById("userInput").value;

  fetch("/ask", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: message }),
  })
    .then(response => response.json())
    .then(data => {
      document.getElementById("botReply").innerText = data.reply;
      speakText(data.reply);  // Optional: speak the bot's response
    });
}

function startListening() {
  const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
  recognition.lang = 'en-US';
  recognition.start();

  recognition.onresult = function(event) {
    const transcript = event.results[0][0].transcript;
    document.getElementById("userInput").value = transcript;
    sendMessage();
  };

  recognition.onerror = function(event) {
    alert("Error: " + event.error);
  };
}

function speakText(text) {
  const utterance = new SpeechSynthesisUtterance(text);
  utterance.lang = "en-US";
  window.speechSynthesis.speak(utterance);
}
<script>
    const micButton = document.getElementById('micButton');

    // Setup speech recognition
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    const recognition = new SpeechRecognition();
    recognition.lang = 'en-US';
    recognition.interimResults = false;
    recognition.maxAlternatives = 1;

    micButton.addEventListener('click', () => {
        recognition.start();
        micButton.textContent = '🎙️ Listening...';
    });

    recognition.onresult = (event) => {
        const speechToText = event.results[0][0].transcript;
        messageInput.value = speechToText;
        sendMessage();  // automatically send the message
        micButton.textContent = '🎤';
    };

    recognition.onerror = (event) => {
        alert('Speech recognition error: ' + event.error);
        micButton.textContent = '🎤';
    };

    recognition.onend = () => {
        micButton.textContent = '🎤';
    };
</script>
