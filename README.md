# 🐝 CLI Spelling Bee (TTS Edition)

A lightweight, Python-powered command-line Spelling Bee game that uses Text-to-Speech (TTS) to speak words aloud.

> **⚠️ Work in Progress (WIP):** This project is currently in active development. Features may be incomplete, and things might break!

---

## ✨ Features

* **Text-to-Speech (TTS) Audio:** Listens to words spoken aloud directly from your terminal—just like a real spelling bee.
* **Pure Python:** Built with Python using standard/accessible TTS libraries with zero bloated UI.
* **Lightweight & Fast:** Runs directly in your command line or terminal.

---

## 🛠️ Prerequisites

Before running the game, make sure you have:

* **Python 3.7+** installed on your system.
* **Working speakers or headphones** (since the words are spoken via TTS!).
* A TTS library installed (e.g., `pyttsx3` or `gTTS` — *update this based on your code*).

---

## 🚀 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd spelling bee
   ```

2. **(Optional) Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🎮 How to Play

Run the main script from your terminal:

```bash
python easy_trust.py
```

1. Listen carefully as the program speaks a word out loud.
2. Type the spelling of the word into the terminal and press **Enter**.
3. See if you got it right and move on to the next word!

---

## 🗺️ Roadmap / To-Do

Since this is a work in progress, here are some things planned or currently being tested:

- [ ] Verify audio output across Windows, macOS, and Linux
- [ ] Add a "repeat word" command
- [ ] Add word definitions and example sentences
- [ ] Include difficulty levels (Easy, Medium, Hard)
- [ ] Track high scores and streaks

---

## 🐛 Known Issues & Troubleshooting

* **No sound playing?** Make sure your system volume is up and your TTS engine (`pyttsx3`, `espeak` on Linux, etc.) is properly installed.
* **Untested code:** Because this is a WIP, edge cases and crashes may happen. Feel free to open an issue if you find a bug!

---

## 🤝 Contributing

Since this project is still in its early stages, suggestions, bug reports, and pull requests are super welcome!

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.
