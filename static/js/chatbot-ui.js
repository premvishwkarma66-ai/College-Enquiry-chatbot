document.addEventListener("DOMContentLoaded", () => {

  const chatToggle = document.getElementById("chat-toggle");
  const chatWidget = document.getElementById("chat-widget");
  const sendBtn = document.getElementById("send-btn");
  const input = document.getElementById("userInput");
  const chatWindow = document.getElementById("chat-window");
  const expandBtn = document.getElementById("expand-btn");

  let welcomed = false;
  let lastMessageDate = null;

  // ---------------- TOGGLE CHAT ----------------
  chatToggle.addEventListener("click", () => {
  const icon = chatToggle.querySelector(".chat-icon");
  const label = chatToggle.querySelector(".chat-label");

  const isHidden = chatWidget.classList.contains("hidden");

  if (isHidden) {
    // OPEN CHAT
    chatWidget.classList.remove("hidden");

    requestAnimationFrame(() => {
      chatWidget.classList.add("show");

      // 🔥 FIX: trigger welcome AFTER chat actually appears
      if (!welcomed) {
        addMessage("Hello 👋 I am the College Enquiry Assistant.", "bot");
        welcomed = true;
      }
    });

    icon.innerText = "❌";
    label.innerText = "Close chat";
  } 
  else {
    // CLOSE CHAT
    chatWidget.classList.remove("show");

    setTimeout(() => {
      chatWidget.classList.add("hidden");
    }, 200);

    icon.innerText = "💬";
    label.innerText = "Chat with us";
  }
});

  // ---------------- FULLSCREEN ----------------
  if (expandBtn) {
    expandBtn.addEventListener("click", () => {
      chatWidget.classList.toggle("fullscreen");
    });
  }

  // ---------------- SEND MESSAGE ----------------
  sendBtn.addEventListener("click", sendMessage);
  input.addEventListener("keypress", e => {
    if (e.key === "Enter") sendMessage();
  });

  // ---------------- DATE HELPERS ----------------
  function isSameDay(d1, d2) {
    return d1.getFullYear() === d2.getFullYear() &&
           d1.getMonth() === d2.getMonth() &&
           d1.getDate() === d2.getDate();
  }

  function formatDateLabel(date) {
    const today = new Date();
    const yesterday = new Date();
    yesterday.setDate(today.getDate() - 1);

    if (isSameDay(date, today)) return "Today";
    if (isSameDay(date, yesterday)) return "Yesterday";

    return date.toLocaleDateString([], {
      day: "2-digit",
      month: "short",
      year: "numeric"
    });
  }

  function relativeTime(fromDate) {
    const seconds = Math.floor((new Date() - fromDate) / 1000);

    if (seconds < 10) return "Just now";
    if (seconds < 60) return `${seconds}s ago`;

    const minutes = Math.floor(seconds / 60);
    if (minutes < 60) return `${minutes} min ago`;

    const hours = Math.floor(minutes / 60);
    return `${hours} hour${hours > 1 ? "s" : ""} ago`;
  }

  // ---------------- ADD MESSAGE ----------------
function addMessage(text, sender) {
  const now = new Date();

  // ---- Date separator ----
  if (!lastMessageDate || !isSameDay(now, lastMessageDate)) {
    const sep = document.createElement("div");
    sep.className = "date-separator";
    sep.innerText = formatDateLabel(now);
    chatWindow.appendChild(sep);
  }

  lastMessageDate = now;

  // ---- Row ----
  const row = document.createElement("div");
  row.className = "msg-row " + (sender === "user" ? "user" : "bot");

  // ---- Avatar ----
  const avatar = document.createElement("img");
  avatar.className = "avatar";

  avatar.src =
    sender === "bot"
      ? "/static/images/college.png"
      : "/static/images/user.png";

  // ---- Bubble ----
  const bubble = document.createElement("div");
  bubble.className = sender === "bot" ? "msg-bot" : "msg-user";

  const msgText = document.createElement("div");
  msgText.innerText = text;

  const time = document.createElement("div");
  time.className = "msg-time";
  time.dataset.timestamp = now.getTime();
  time.innerText = relativeTime(now);

  bubble.appendChild(msgText);
  bubble.appendChild(time);

  row.appendChild(avatar);
  row.appendChild(bubble);

  chatWindow.appendChild(row);
  chatWindow.scrollTop = chatWindow.scrollHeight;
}


  // ---------------- AUTO UPDATE TIMES ----------------
  function refreshAllTimestamps() {
    const times = document.querySelectorAll(".msg-time");

    times.forEach(el => {
      const ts = parseInt(el.dataset.timestamp, 10);
      if (!isNaN(ts)) {
        el.innerText = relativeTime(new Date(ts));
      }
    });
  }

  // update every 60 seconds
  setInterval(refreshAllTimestamps, 60000);

  // ---------------- API CALL ----------------
  async function sendMessage() {
    const msg = input.value.trim();
    if (!msg) return;

    addMessage(msg, "user");
    input.value = "";

    const res = await fetch("/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: msg })
    });

    const data = await res.json();
    addMessage(data.reply, "bot");
  }

});
