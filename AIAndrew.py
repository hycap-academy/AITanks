
import inspect
if "rungame" not in inspect.getmodule(inspect.stack()[0])._filesbymodname["__main__"]:
    import rungame

class AI:
    def __init__(self):
        print(__name__ + " AI Loaded")
        self.image = "DozerBlue.png"

    def turn(self):
        enemy = self.robot.findClosestEnemy()
        if enemy != None:
            dir = self.robot.getDirection(enemy)
            #print(dir)
            dis = self.robot.getDistance(enemy)
            if dir > 5:
                self.robot.turnLeft()
                #print("turn left")
            elif dir < -5:
                self.robot.turnRight()
                #print("turn right")
            elif dis <= 225 and self.robot.health > 90:
                self.robot.fireProjectile(dir)
            elif self.robot.energy >=25 and self.robot.health <=90:
                self.robot.repair(self.robot.energy/4)
            elif dis > 225 and self.robot.health > 90:
                self.robot.moveForward()
                    #print("move forward")
            elif dis < 275 and self.robot.energy <25 and self.robot.health > 90:
                self.robot.moveForward(-2)
            

            #print("mydir:", self.robot.direction, " getDir:", dir, " getDist: ", dis )
            
        
