# Disappearing Text Writing App

A minimalist, high-stakes desktop writing application built with Python and Tkinter. Designed to overcome writer's block and over-editing, the app challenges you to keep typing—if you stop for more than **5 seconds**, all of your progress vanishes.

Built as a portfolio project for **Day 90 of the 100 Days of Code: The Complete Python Pro Bootcamp**, refactored from scratch using modular Object-Oriented Programming (OOP) and event-driven architecture.

---

## Features

- **5-Second Inactivity Wipe:** Automatically clears the editor if no valid writing activity occurs within 5 seconds of your first keystroke.
- **Live Countdown Feedback:** Displays a real-time countdown timer (`Time left: 5s`) so you always know how much time remains before deletion.
- **Smart Input Filtering:** Ignores non-character modifier keys (`Shift`, `Ctrl`, `Alt`, `Caps Lock`) so accidental key taps do not falsely reset the timer.
- **Clipboard Paste Detection:** Listens for virtual `<<Paste>>` events so pasting text via mouse or keyboard shortcuts properly resets the countdown.
- **Distraction-Free Dark Mode UI:** Clean, responsive layout built with centralized styling constants and graceful window-close cleanup (`WM_DELETE_WINDOW`).

---

## Architecture & Engineering Decisions

Rather than placing all UI widgets, global variables, and timer loops inside a single script, this application follows **Separation of Concerns** across four focused modules:

```text
disappearing_text_app/
├── main.py      # Application entry point
├── config.py    # Centralized styling constants and timer configuration
├── timer.py     # Decoupled, non-blocking countdown state machine
└── ui.py        # Tkinter window layout, event listeners, and UI handlers
```

### Key Design Patterns Used
- **Non-Blocking Event Loop (`.after` / `.after_cancel`):** Avoids `time.sleep()` or blocking `while` loops that freeze desktop interfaces, scheduling 1-second ticks directly on Tkinter's native event loop instead.
- **Callback Decoupling & Dependency Injection:** `InactivityTimer` (`timer.py`) has zero dependencies on specific UI widgets. It communicates state changes exclusively through `on_tick` and `on_timeout` callbacks injected by `App` (`ui.py`).
- **PEP 8 & PEP 257 Compliance:** Uses full Python type annotations, guard clauses for clean control flow, and standardized module/class docstrings.

---

## Getting Started

### Prerequisites
- **Python 3.10+** (Uses Python's built-in `tkinter` library—no external `pip` packages required.)

### Installation & Running
1. Clone the repository:
   ```bash
   git clone https://github.com/Sammy-Softway/web-dev-showcase.git
   cd disappearing-text-app
   ```
2. Run the application:
   ```bash
   python main.py
   ```

---

## Future Enhancements
- [ ] Add progressive text color fading as the timer approaches `0s`
- [ ] Allow users to select custom inactivity durations (`5s`, `10s`, `15s`)
- [ ] Add a "Save Session" export option once a target word count or writing sprint is completed


## Project Reflection

### 1. What was easy?
**Answer:** Breaking the project down into logical stages and separating the styling constants into `config.py` felt very straightforward. Setting up the base Tkinter window and getting the initial dark-mode layout on screen came together pretty quickly once I organized the widgets inside a single setup method.

### 2. What was hard?
**Answer:** Wrapping my head around event-driven programming and reading Tkinter's documentation was definitely the toughest part. Moving away from normal top-to-bottom Python scripts—where you call every function yourself—to passing callback functions without parentheses and letting `mainloop()` and `.after()` trigger them behind the scenes took me a while to truly understand. Getting the indentation and state flow right inside the timer loop without causing overlapping alarms also took careful debugging.

### 3. How I might improve for the next project? / What I would do differently?
**Answer:** Next time, I want to spend a little more time upfront mapping out the exact signatures of library methods before writing code, rather than guessing parameters and relying on IDE warnings to catch mismatches. I also want to get into the habit of declaring all my class attributes cleanly inside `__init__` from the very first draft instead of refactoring them later.

### 4. What was my biggest learning from today?
**Answer:** Learning how callbacks, Dependency Injection, and non-blocking event loops actually work under the hood. Instead of stuffing everything into one messy script with `time.sleep()`, keeping `InactivityTimer` completely separate from the UI widgets showed me how real software is structured—and why writing clean, decoupled code matters just as much as making the program run.

