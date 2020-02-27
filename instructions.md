Python Tank AI Instruction
==========================

Python Tank AI is a game made in Python where each player creates an AI program and pits their AI program against other players.  The game is created in Python, but the player does not need to be an expert in Python to participate.  

Tournament
----------
The first tournament will be held on May 29th, 2020 (Friday).  Location TBD.  Remote participants may submit their AI tank code via email to donhyun@hycapacademy.com by May 22nd, 2020.  For more information, contact donhyun@hycapacademy.com.

Objective
---------
Here is how to win:
1.  Destroy the other tank by bombing, shooting, or ramming the opponents before the time limit is up.  
2.  If more than one tank is alive when the time limit is up, the winner is the tank that has claimed the most tiles.
3.  If active tanks have the same number of tiles, the winner is the tank that has the most energy+health points.

In the case where all active tanks have the same number of tiles and energy+health points, it is a tie.

Time Limit
----------
The default time limit is set to 5 minutes, but may be changed for different tournaments/competitions.

Required Skills
---------------
It will help if the player understands some coding fundamentals such as if/then statements and loops.  It will also help if the player understands some geometry such as angle measurements in degrees and the pythagorean theorem.

How to get started
------------------
The best way to get started is to run the game using Visual Studio Code with the Python extension installed.  Here is a quick How-To.

1. [Install and Setup VS Code for Python](./VSCode_Setup.md)
2. Make a copy of AILevel0.py and rename it to using your name:  e.g.  AIJeff1.py  (Please note that all AI Tank files need to start with the prefix "AI".  
3. write code under the def turn(self): section.  That is the only section that you can change.  See the documentation below for how to access the methods and properties.
4. Peek at the other provided AI files to see how they work.  
5. Create your own AI.

Rules
-----
You may read anything that is in the game and incorporate it into your AI algorithm.  Many interfaces are given for your convenience in reading information about objects in play.
You may only use the listed APIs to take action (e.g. attack, move, etc).  Otherwise, you'd be able to find the opponent and remove all of their health which wouldn't make for a very fun game.
If you have creative strategies that may be questionable, please contact us and we'll make a rule clarification.

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
|enemy = self.robot.findClosestEnemy  (object)| returns your opponent as an object.|Energy: Does not take any energy|
|dir = self.robot.getDirection(enemy)  (int) | tells you the relative direction of an object.  If an enemy is at your 9 o'clock, you would get 90. If your enemy is at 3 o'clock, you would get back -90|Does not take any energy|
|dis = self.robot.getDistance(enemy)  (int) | tells you how far away your enemy is.  The board is 600x600 | Does not take any energy|
|self.robot.x() (int 0-600)| tells you x coordinate of your robot. The board is 600x600 | Does not take any energy|
|self.robot.y() (int 0-600)| tells you y coordinate of your robot. The board is 600x600 | Does not take any energy|
|self.robot.direction int | tells you direction of your robot in degrees.  0 is North.  90 is facing West.  -90 is Facing East | Does not take any energy|
|self.robot.energy (int 1-100) | tells how much energy the player's robot has| Does not take any energy|
|self.robot.health (int 1-100) | tells how much health the player's robot has| Does not take any energy|
|self.robot.shield (True/False) | tells you if the shield is on or not| Does not take any energy|
|tiles = self.robot.tiles | gives you the array of tiles | Does not take any energy |
|self.robot.myTiles() | returns an integer and tells you how many tiles belong to the player | Does not take any energy |
|t = self.robot.findClosestNewTile() | returns the closest tile that is now owned by the player.  It's possible to use getDirection and getDistance to get the direction and distance to the tile similar to with an enemy. | Does not take any energy |

#### Tile Object
|Syntax|Description|
|------|-----------|
| t.x()| returns the x coordinate of the tile.|
| t.y()| returns the y coordinate of the tile.|
| t.player()| returns the owning player of this tile.|


### Attack
|Syntax|Description|Energy Required|Damage|
|------|-----------|---------------|------|
|self.robot.fireProjectile(dir) | fires a projectile in a relative direction.  If you fireProjectile(0), it will fire straight forwad from the tank| Each time you fire, it costs 10 energy points. |Each projectile takes 1 health point.|
|self.robot.ram()|rams your enemy.Your distance must be less than 10 away. | takes 10 energy points | rams the enemy for 5-15 points of damage. This will also cause 0-5 points of health damage to you|
|self.robot.dropBomb(enemy) |launches a bomb to where your enemy is located. |40 energy points |Does 5-20 points of health damage.|

