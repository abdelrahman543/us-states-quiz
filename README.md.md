# 🗺️ US States Quiz

An interactive geography quiz game built with Python's Turtle module. Type the name of a US state and watch it appear in the correct location on a blank map. Try to guess all 50!

---

## 🎮 How to Play

1. A blank US map appears on screen
2. A prompt asks you to guess a state
3. Type a state name correctly → it appears on the map in the right location
4. Type **"Exit"** at any time to quit
5. A `states_to_learn.csv` file is automatically saved with all the states you missed

---

## ✨ Features

- 🗺️ **Interactive Map** — correct guesses are plotted directly on the US map
- 📊 **Progress Counter** — shows how many states you've guessed out of 50
- 💾 **Miss Tracker** — saves unguessed states to a CSV so you can study them later
- 📂 **CSV-powered** — state names and coordinates loaded from a data file

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3 | Core language |
| Turtle | Built-in graphics & UI |
| Pandas | CSV reading & writing |

---

## 🚀 Getting Started

### 1. Install dependencies
```bash
pip install pandas
```

### 2. Run the game
```bash
python main.py
```

> Make sure `50_states.csv` and `blank_states_img.gif` are in the same directory as `main.py`.

---

## 📁 Project Structure

```
us-states-quiz/
├── main.py                # Game logic
├── 50_states.csv          # State names & map coordinates
├── blank_states_img.gif   # Blank US map image
├── states_to_learn.csv    # Auto-generated — missed states
└── README.md
```

---

## 📸 Preview

![US States Quiz Preview](preview.png)

---

## 📌 Roadmap

- [ ] Add a timer for speed challenge mode
- [ ] Show final score screen on completion
- [ ] Add hint system (first letter of state)
- [ ] Expand to world countries map

---

## 👨‍💻 Author

**Abdelrahman**
