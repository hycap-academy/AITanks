
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
            else:
                if dis < 200:
                    self.robot.fireProjectile(dir)
                else:
                    self.robot.moveForward()
                    #print("move forward")
            
            

            #print("mydir:", self.robot.direction, " getDir:", dir, " getDist: ", dis )
            
        
