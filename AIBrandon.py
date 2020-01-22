
import inspect
if "rungame" not in inspect.getmodule(inspect.stack()[0])._filesbymodname["__main__"]:
    import rungame

class AI:
    def __init__(self):
        print(__name__ + " AI Loaded")
        self.image = "DozerBlue.png"
    
    def turn(self):
        enemy = self.robot.findClosestEnemy()
        dir = self.robot.getDirection(enemy)
        dis = self.robot.getDistance(enemy)
        print(dir)

        if dir > 3:
            self.robot.turnLeft(5)
        if dir < -3:
            self.robot.turnRight(5)
        else:
            if dis > 250:
                self.robot.moveForward(5)
            else:
                self.robot.fireProjectile(dir)
            


