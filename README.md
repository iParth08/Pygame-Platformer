# 🕹️ Mr Platformer - Scalable Pygame Project

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)  
![Pygame](https://img.shields.io/badge/Library-Pygame-green?logo=pygame)  
![License](https://img.shields.io/badge/License-MIT-yellow.svg)  
![Contributions](https://img.shields.io/badge/Contributions-Welcome-orange)

---

## 📝 About the Game

**Mr. Platformer** is a **2D side-scrolling platformer** built in Python with Pygame.  
Jump, run, dodge fire traps 🔥, and explore a scrolling world of blocks.  
This project started as a way to **learn game development concepts** while keeping it fun and simple.

---

It has been fully refactored to follow **SOLID principles** and designed for **scalability**, so new features (enemies, traps, levels, story, etc.) can be added with minimal changes to existing code.

---

## 🎥 Demo

_Coming Soon… (insert your GIF/video here)_  
![Game Demo](demo.gif)

---

## 🛠️ Tech Stack

- 🐍 **Python 3.x**
- 🎨 **Pygame** (graphics, input, sprite handling)
- 🖼 **Free Assets** (sprites, backgrounds, tiles)

---

## 📂 File Structure

```python

project/
├─ assets/ # put your images, sprites, audio here
├─ maps/
| ├─ level_x.json # level maps data
├─ src/
│ ├─ main.py # Entry point
│ ├─ game.py # Game Controls
│ ├─ config.py # Constants
│ ├─ utils.py # Helper Functions
│ ├─ objects.py # Blocks, obstacles etc
│ ├─ player.py # Player, Enemy
│ ├─ traps.py
│ ├─ renderer.py # Draw Functions
│ ├─ level_loader.py # Map Loader
│ └─ input_handler.py # Input Mechanism
├─ requirements.txt
├─ structure.txt
└─ README.md
```

---

## 🖼️ Module Connection Diagram

Below is a simplified ASCII UML diagram showing how the modules interact

```bash
          ┌────────────┐
          │  main.py   │
          └─────┬──────┘
                │ starts game
                ▼
          ┌────────────┐
          │  Game.py   │
          └─────┬──────┘

manages │ │ loads
│ ▼
│ LevelLoader
│ │
▼ ▼
┌─────────────┐ ┌───────────────┐
│ Camera.py │<─────>│ Entities │
│ (offsets) │ │ (Player, │
└─────┬───────┘ │ Enemies, │
│ │ Blocks, etc)│
│ └──────┬────────┘
│ draws │ update/draw
▼ ▼
┌─────────────────────────────────┐
│ Renderer / Screen │
└─────────────────────────────────┘
```

---

## 🛠️ New Changes & Scalability Features

1. **Separation of Concerns**

   - Each game object (Player, Enemy, Trap, Block) lives in its own file under `entities/`.
   - Game flow (loop, updates, rendering) is in `core/game.py`.
   - Camera movement is fully modularized (`core/camera.py`).

2. **Level Loading from JSON**

   - Levels are defined in **JSON format** (`levels/level1.json`).
   - Data-driven design allows adding new levels without touching the game code.
   - Example JSON structure:
     ```json
     {
       "blocks": [
         [0, 2],
         [1, 2]
       ],
       "fires": [
         [6, 4],
         [8, 7]
       ],
       "player_spawn": [2, 5],
       "goal": [18, 20]
     }
     ```

3. **Camera System**

   - Side-scrolling with horizontal + vertical support.
   - Option to lock camera within level boundaries.

4. **Entity Abstraction**

   - Base class for all entities (`GameObject`) ensures consistent interface.
   - Easy to extend with new entities (new enemy types, power-ups, collectibles).

5. **SOLID Principles**

   - **S**ingle Responsibility → Each class has one clear responsibility.
   - **O**pen/Closed → New enemies, traps, and blocks can be added without modifying existing code.
   - **L**iskov Substitution → All entities inherit from base classes and can be swapped seamlessly.
   - **I**nterface Segregation → Entities expose only the methods they need (`update`, `draw`).
   - **D**ependency Inversion → High-level modules (Game) depend on abstractions (interfaces), not concrete implementations.

6. **Placeholders for Future Features**
   - ✅ Multiple enemies & enemy AI
   - ✅ Different terrains & traps
   - ✅ Sound effects & background music
   - ✅ Player stats & HUD system
   - ✅ Storyline text captions
   - ✅ Multiple levels with progression

---

## 🚀 How to Run

0. Clone the repository

   ```bash
   git clone https://github.com/yourusername/mr-platformer.git
   cd mr-platformer
   ```

1. Install dependencies:

   ```bash
   pip install pygame
   ```

2. Go to src and run main.py

   ```bash
   cd src
   python3 main.py
   ```

---

## 🎮 How to Play

- ⬅️ ➡️ Arrow Keys → Move left / right

- ␣ Space → Jump (double jump allowed!)

- 🔥 Avoid fire traps → They’ll hurt you!

- 🎯 Objective → Survive, jump around, and vibe

## 📚 Concepts Learned

This project helped me practice & understand:

- ⚡ Game loops and FPS control

- 🖼 Sprite sheets & animations

- 🌍 Camera offset & scrolling world

- 🧱 Terrain blocks & traps

- 🪂 Gravity & jump physics

- 🎭 Collision detection with masks

- 💡 Object-Oriented Programming in game dev

## 🌟 Upcoming Improvements

- Add enemies 👾

- Power-ups 🍄

- Multiple levels & checkpoints

- Background music & sound effects 🎵

## Referenced Tutorial for Base

👉 https://youtu.be/6gLeplbqtqg?si=_oJFRfylRYFLTAf3&t=1098

---

## 🧩 Future Roadmap

- Add _enemy AI behaviors_ (patrolling, chasing).
- Implement physics improvements (friction, slopes, wall jumps).
- Create **UI system** (menus, pause, HUD, stats).
- Add **networking support** (multiplayer modes).
- Integrate **save/load system** for progress.
