
import inspect
if "rungame" not in inspect.getmodule(inspect.stack()[0])._filesbymodname["__main__"]:
    import rungame

class AI:
    def __init__(self):
        print(__name__ + " AI Loaded")
        self.image = "tankred3.png"

    def turn(self):
        enemy = self.robot.findClosestEnemy()
        dir = self.robot.getDirection(enemy)
        dis = self.robot.getDistance(enemy)
        print(dis)
        if dis > 10:
            if dir > 3:
                self.robot.turnLeft(5)
            elif dir < -3:
                self.robot.turnRight(5)
            else:
                self.robot.moveForward(5)
            if dis < 300 and self.robot.shield==False:
                self.robot.shieldOn()
        else:
            if dir < 90 and dir > -90:
                self.robot.ram()
            else: 
                self.robot.moveForward(-3)
