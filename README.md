# 🐍 Simple snake game - Python
![Screenshot from the game.](https://github.com/Pawelo112/Simple-snake-game-in-Python/assets/121107616/73b78187-7075-47e6-a0d7-ac1307deae7e)

## 📖 Description and rules
This is a simple snake game that I made in Python using Turtle module, during **100 days of code** Python course.

The rules of snake:
+ 🎮You control the snake with arrows to move up⬆️, down⬇️, left⬅️ and right➡️.
+ ⛔You cannot move in the opposite direction - for example you cannot move down if head of the snake is heading up.
+ 🍎You collect the food, which position is randomized - each piece of food gives you one point and makes snake longer each time.
+ 🏆Your main goal is to have the highest score possible (you can see your current score at the top of the screen).
+ ❎**The game is over** when:
  + Snake collides with the wall.
  + Snake collides with its own body.
+ 🔁When you lost the game, you have to click on the screen and launch the app one more time to play again.

## 📁 Files description
+ **[main.py](https://github.com/Pawelo112/Simple-snake-game-in-Python/blob/main/main.py)** - Main file of the app. Here the objects for food, snake, scoreboard and screen are created and collision is being detected. From the important things you can edit screen size here or change the speed of the game.
  
+ **[food.py](https://github.com/Pawelo112/Simple-snake-game-in-Python/blob/main/food.py)** - Here the food object is being represented and its position and color is being randomized. You can add any colors to the colors list as long as Turtle module supports it.
  
+ **[scoreboard.py](https://github.com/Pawelo112/Simple-snake-game-in-Python/blob/main/scoreboard.py)** - This file contains all methods connected to the scoreboard like updating score and displaying **GAME OVER** screen.
  
+ **[snake.py](https://github.com/Pawelo112/Simple-snake-game-in-Python/blob/main/snake.py)** - This file collects all methods and things connected to the snake object like creating small snake at the start and adding new "segments" of it, which is used after eating one piece of food by snake.

## 🖥️ Usage
You can find the latest release here: [releases](https://github.com/Pawelo112/Simple-snake-game-in-Python/releases)  
You can download exe file to play and test the game or whole source code to edit this game on your own 🤓.  

Unfortunately windows defender and other anti-viruses detects **Snake.exe** file as a virus because it was made with pyinstaller and it is known issue with exe files made with it and there isn't much that I can do about it.
## 📝 License

Copyright © 2024 [Paweł Marcinkowski](https://github.com/Pawelo112).  
This project is [MIT](https://github.com/Pawelo112/Simple-snake-game-in-Python/blob/main/LICENSE) licensed.
