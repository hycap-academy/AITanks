
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

        if self.robot.health < 50:
            self.robot.repair(self.robot.energy)
            
        if dir > 3:
            self.robot.turnLeft(5)
        if dir < -3:
            self.robot.turnRight(5)
        else:
            if dis > 400:
                self.robot.moveForward(10)
            else:
                self.robot.fireProjectile(dir)

