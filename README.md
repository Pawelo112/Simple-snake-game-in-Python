# 🐍 Simple snake game - Python
![Screenshot from the game.](https://github.com/Pawelo112/Simple-snake-game-in-Python/assets/121107616/73b78187-7075-47e6-a0d7-ac1307deae7e)

## 📖 Description and rules
This is a simple snake game that I made in Python using Turtle module, during **100 days of code** Python course.

The rules of snake:
+ 🎮You control a snake with arrows to move up⬆️, down⬇️, left⬅️ and right➡️.
+ ⛔You cannot move in the opposite direction - for example you cannot move down if head of the snaka is heading up.
+ 🍎You collect the food, which position is randomized - each piece of food gives you one point and makes snake longer each time.
+ 🏆Your main goal is to have the highest score possible (you can see your current score at the top of the screen).
+ ❎**The game is over** when:
  + Snake collides with the wall.
  + Snake collides with its own body.
+ 🔁When you lost the game, you have to click on the screen and launch the app to play again.

## 📁 Files description
+ **[main.py](https://github.com/Pawelo112/Simple-snake-game-in-Python/blob/main/main.py)** - Main file of the app. Here the objects for food, snake, scoreboard and screen are created and collision is being detected. From the important things you can edit screen size here or change speed of the game.
+ **[food.py](https://github.com/Pawelo112/Simple-snake-game-in-Python/blob/main/food.py)** - Here the food object is being represented and its position and color being randomized. You can add any colors to the colors list as long as Turtle module supports it.
+ **[scoreboard.py](https://github.com/Pawelo112/Simple-snake-game-in-Python/blob/main/scoreboard.py)** - This file contains all methods connected to the scoreboard like updating score and displaying **GAME OVER** screen.
+ **[snake.py](https://github.com/Pawelo112/Simple-snake-game-in-Python/blob/main/snake.py)** - This file collects all methods and things connected to the snake object like creating small snake at the start and creating new "segments" of it, which is used after eating one piece of fodd by snake.
