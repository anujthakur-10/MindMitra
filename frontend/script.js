async function login() {
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    try {
        await auth.signInWithEmailAndPassword(email, password);
        window.location.href = "chat.html";
    } catch (error) {
        alert(error.message);
    }
}

async function signup() {
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    try {
        await auth.createUserWithEmailAndPassword(email, password);
        window.location.href = "chat.html";
    } catch (error) {
        alert(error.message);
    }
}

async function googleLogin() {
    const provider = new firebase.auth.GoogleAuthProvider();
    try {
        await auth.signInWithPopup(provider);
        window.location.href = "chat.html";
    } catch (error) {
        alert(error.message);
    }
}

async function guestLogin() {
    try {
        await auth.signInAnonymously();
        window.location.href = "chat.html";
    } catch (error) {
        alert(error.message);
    }
}

async function logout() {
    await auth.signOut();
    window.location.href = "login.html";
}

auth.onAuthStateChanged(user => {
    if (!user && window.location.pathname.includes("chat.html")) {
        window.location.href = "login.html";
    }
});

async function sendMessage() {
    const userInput = document.getElementById("userInput").value.trim();
    if (userInput === "") return;

    displayMessage("user", userInput);
    document.getElementById("userInput").value = "";

    const response = await fetch('http://127.0.0.1:8000/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: userInput })
    });
    const data = await response.json();
    displayMessage("bot", data.reply);
}

// Voice Input Function
function startListening() {
    const recognition = new window.webkitSpeechRecognition(); // Or SpeechRecognition
    recognition.continuous = false;
    recognition.lang = 'en-IN';
  
    recognition.onresult = function(event) {
      const transcript = event.results[0][0].transcript;
      console.log("Heard:", transcript);
      sendMessage(transcript);
    };
  
    recognition.start();
  }
  

function displayMessage(sender, message) {
    const chatBox = document.getElementById("chatBox");
    const messageDiv = document.createElement("div");

    // Add alignment class
    messageDiv.classList.add(sender === "user" ? "text-right" : "text-left");

    // Create a message bubble
    const bubble = document.createElement("div");
    bubble.classList.add("inline-block", "px-4", "py-2", "rounded-lg", "max-w-xl", "text-left", "whitespace-pre-wrap");
    bubble.classList.add(sender === 'user' ? "bg-blue-200" : "bg-green-200");

    // Format markdown and fix spacing
    const html = marked.parse(message.trim());
    bubble.innerHTML = html;

    // Optional: fine-tune line height and margin for compact look
    bubble.style.lineHeight = "1.4";
    bubble.style.margin = "0";

    messageDiv.appendChild(bubble);
    chatBox.appendChild(messageDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
}


function startNewChat() {
    document.getElementById("chatBox").innerHTML = "";
}
