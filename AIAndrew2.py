
import inspect
if "rungame" not in inspect.getmodule(inspect.stack()[0])._filesbymodname["__main__"]:
    import rungame


#  you get 5 energy points each round
#  self.robot.moveForward(speed)  - moves forward
#           Energy: takes half of the speed in energy.  10 is the max speed.  It costs 5 energy points to move at speed=10
#  self.robot.turnLeft(speed) - turns left
#           Energy: takes half of the speed in energy.  10 is the max speed.  It costs 5 energy points to move at speed=10
#  self.robot.turnRight(speed) - turns right
#           Energy: takes half of the speed in energy.  10 is the max speed.  It costs 5 energy points to move at speed=10
#  self.robot.shieldOn() - turns on your shield.  Shield turns off if you have less than 50 energy points.  
#           Energy: Keeping the shield on takes 3 energy points each round
#  enemy = self.robot.findClosestEnemy returns your opponent as an object.  
#           Energy: Does not take any energy
#  dir = self.robot.getDirection(enemy) - tells you the relative direction of an object.  If an enemy is at your 9 o'clock, you would get 90.  
#           if your enemy is at 3 o'clock, you would get back -90
#           Energy:  DOes not take any energy
#  dis = self.robot.getDistance(enemy) - tells you how far away your enemy is.  The board is 600x600
#           Energy:  DOes not take any energy
#  self.robot.fireProjectile(dir) - fires a projectile in a relative direction.  If you fireProjectile(0), 
#           it will fire straight forwad from the tank
#           Energy:  each time you fire, it costs 10 energy points.  
#           Damage: Each projectile takes 1 health point.
#  self.robot.ram() - rams your enemy.Your distance must be less than 10 away. 
#           Energy:  takes 10 energy points
#           Damage: rams the enemy for 5-15 points of damage. This will also cause 0-5 points of health damage to you
#  self.robot.repair(points)  - repairs your tank.  The number of points you can repair is unlimited (up to 100).  
#           Energy:  The number of heal points is the number of energy points that it costs
#  self.robot.dropBomb(enemy)  - launches a bomb to where your enemy is located. 
#           Energy:  40 energy points
#           Damage:  Does 5-20 points of health damage.

class AI:
    def __init__(self):
        print(__name__ + " AI Loaded")
        self.image = "DozerBlue.png"

    def turn(self):
        enemy = self.robot.findClosestEnemy()
        if enemy != None:
            dir = self.robot.getDirection(enemy)
            #print(dir)

            self.robot.fireProjectile(dir)
                    #print("move forward")
            
            

            #print("mydir:", self.robot.direction, " getDir:", dir, " getDist: ", dis )
            
        
