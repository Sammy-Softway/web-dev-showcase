# Breakout Arcade Game (Python & Turtle)

A classic arcade Breakout game built from scratch in Python using the built-in `turtle` module and clean Object-Oriented Programming (OOP) architecture.

## Features
- **Dual Controls:** Smooth paddle movement supporting both keyboard (`Left` / `Right` arrow keys) and mouse cursor tracking.
- **Custom Collision Physics:** Accurate X/Y bounding-box detection for walls, paddle edges, and brick faces/sides.
- **Multi-Level Progression:** 3 escalating levels with dynamically increasing brick rows and progressive ball speed-ups.
- **Persistent Top 5 Leaderboard:** Saves high scores and 3-letter player initials locally using JSON (`scores.json`).

## Project Structure
- `main.py` — Clean application entry point.
- `game_manager.py` — Orchestrates the game loop, screen setup, input bindings, and collision checks.
- `paddle.py` — Manages paddle rendering and boundary-clamped movement.
- `ball.py` — Handles ball velocity, bouncing, speed scaling, and life resets.
- `brick_manager.py` — Generates and manages multi-row colored brick grids.
- `scoreboard.py` — Tracks score, lives, levels, end-game banners, and JSON score persistence.

## How to Run
No external packages required—uses only Python's standard library (`turtle`, `json`, `time`).

1. Clone the repository:
   ```bash
   git clone https://github.com/Sammy-Softway/web-dev-showcase.git
   cd breakout-game
   ```
2. Run the game:
   ```bash
   python main.py
   ```


## Project Reflection & Takeaways

### 1. What was easy?

Answer: Setting up the project structure and building the basic visual components using Python's turtle module went pretty smoothly once I had my plan mapped out. Creating separate classes for the paddle, ball, bricks, and scoreboard felt natural, and getting the initial screen, colors, and grid of bricks to show up on screen was straightforward once I understood how tracer(0) and update() work together.

### 2. What was hard?

Answer: Getting the collision math and edge cases right took the most thought. At first, I assumed turtle's built-in distance() method would handle everything, but I quickly realized wide rectangles like the paddle and bricks need proper X and Y bounding-box math so the ball doesn't pass through the outer edges. I also had to think carefully about subtle bugs—like keeping the paddle from sliding off-screen, stopping the ball from bouncing twice inside the paddle, and making sure removing bricks from a list while looping through it didn't skip items.

### 3. How I might improve for the next project? / What I would do differently?

Answer: Next time, I'd map out the exact coordinate math and constants on paper before coding the collision logic so I spend less time tweaking hardcoded numbers later. I'd also design multi-level scaling and reusable helper methods right from the start instead of retrofitting them at the end, and make more frequent, smaller Git commits after finishing each individual stage.

### 4. What was my biggest learning from today?

Answer: My biggest takeaway is how much cleaner and easier to debug a game becomes when each class has one clear job and GameManager orchestrates how they interact. On the technical side, I really internalized how to think in coordinates (xcor() and ycor() from object centers), how to safely mutate a list by iterating over a shallow copy ([:]), and how to avoid "magic numbers" by deriving boundaries from constants.