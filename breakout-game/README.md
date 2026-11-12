1. What was easy?

Answer: Setting up the project structure and building the basic visual components using Python's turtle module went pretty smoothly once I had my plan mapped out. Creating separate classes for the paddle, ball, bricks, and scoreboard felt natural, and getting the initial screen, colors, and grid of bricks to show up on screen was straightforward once I understood how tracer(0) and update() work together.

2. What was hard?

Answer: Getting the collision math and edge cases right took the most thought. At first, I assumed turtle's built-in distance() method would handle everything, but I quickly realized wide rectangles like the paddle and bricks need proper X and Y bounding-box math so the ball doesn't pass through the outer edges. I also had to think carefully about subtle bugs—like keeping the paddle from sliding off-screen, stopping the ball from bouncing twice inside the paddle, and making sure removing bricks from a list while looping through it didn't skip items.

3. How I might improve for the next project? / What I would do differently?

Answer: Next time, I'd map out the exact coordinate math and constants on paper before coding the collision logic so I spend less time tweaking hardcoded numbers later. I'd also design multi-level scaling and reusable helper methods right from the start instead of retrofitting them at the end, and make more frequent, smaller Git commits after finishing each individual stage.

4. What was my biggest learning from today?

Answer: My biggest takeaway is how much cleaner and easier to debug a game becomes when each class has one clear job and GameManager orchestrates how they interact. On the technical side, I really internalized how to think in coordinates (xcor() and ycor() from object centers), how to safely mutate a list by iterating over a shallow copy ([:]), and how to avoid "magic numbers" by deriving boundaries from constants.