# VeryCold

This game is like SuperHot and Wolfenstein 3D combined, played on a ILI9341 TFT with Raspberry Pi.

The objective is to escape various sized mazes, while keeping a positive health (shown in upper-left corner). The player spawns in a 5x5 maze, and after reaching the goal (green square), the player upgrades to a 7x7 maze, 9x9 maze, and so on.

Health decreases at 5 per bullet from enemies (red) on contact. Health increases at 3 per bullet that successfully hits an enemy. Health resets to 100 after completing a maze, and decreases even quicker if an enemy touches the player.



Notes: Schematic is not accurate to what the real wiring is like. I'll update soon. Also, Wolfenstein 3D has finite ammo, whereas this game currently has infinite ammo.

Final project for Quarter 4 Robotics
