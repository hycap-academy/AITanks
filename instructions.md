Python Tank AI Instruction
==========================

Python Tank AI is a game made in Python where each player creates an AI program and pits their AI program against other players.  The game is created in Python, but the player does not need to be an expert in Python to participate.  

Required Skills
---------------
It will help if the player understands some coding fundamentals such as if/then statements and loops.  It will also help if the player understands some geometry such as angle measurements in degrees and the pythagorean theorem.

How to get started
------------------
The best way to get started is to run the game using Visual Studio Code with the Python extension installed.  Here is a quick How-To.

[Install and Setup VS Code for Python](./VSCode_Setup.md)

## Downloading

[Download and Install Git](./InstallGit.md)

## Commands
Python Tank AI is a real time game.  Each AI player starts with 100 health points and 0 energy points.  Each player gets 5 energy points each round.  The player creates an AI script that uses those energy points by moving, attacking, repairing, or using shields.  Energy can be stored up to 100 points.  

### Moving

|Syntax|Description|Energy Required|
|------|-----------|---------------|
self.robot.moveForward(speed)|moves forward or backward.  Speed can be between -10 and 10|takes half of the speed in energy.    It costs 5 energy points to move at speed=10|
|self.robot.turnLeft(speed)|turns left.  Speed can be between -10 and 10| takes half of the speed in energy.  It costs 5 energy points to move at speed=10|
|self.robot.turnRight(speed)|turns right.  Speed can be between -10 and 10| takes half of the speed in energy.  It costs 5 energy points to move at speed=10|

### Defense
|Syntax|Description|Energy Required|
|------|-----------|---------------|
|self.robot.shieldOn()|turns on your shield.  Shield turns off when you have less than 50 energy points. |Keeping the shield on takes 3 energy points each round|
|self.robot.repair(points)|repairs your tank.  The number of points you can repair is up to 100.  Player health maximum is 100.|The number of heal points is the number of energy points that it costs|


### Get Information
|Syntax|Description|Energy Required|
|------|-----------|---------------|
|enemy = self.robot.findClosestEnemy| returns your opponent as an object.|Energy: Does not take any energy|
|dir = self.robot.getDirection(enemy) | tells you the relative direction of an object.  If an enemy is at your 9 o'clock, you would get 90. If your enemy is at 3 o'clock, you would get back -90|Does not take any energy|
|dis = self.robot.getDistance(enemy) | tells you how far away your enemy is.  The board is 600x600 | Does not take any energy|

### Attack
|Syntax|Description|Energy Required|Damage|
|------|-----------|---------------|------|
|self.robot.fireProjectile(dir) | fires a projectile in a relative direction.  If you fireProjectile(0), it will fire straight forwad from the tank| Each time you fire, it costs 10 energy points. |Each projectile takes 1 health point.|
|self.robot.ram()|rams your enemy.Your distance must be less than 10 away. | takes 10 energy points | rams the enemy for 5-15 points of damage. This will also cause 0-5 points of health damage to you|
|self.robot.dropBomb(enemy) |launches a bomb to where your enemy is located. |40 energy points |Does 5-20 points of health damage.|

