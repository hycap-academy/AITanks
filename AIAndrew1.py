import inspect
if "rungame" not in inspect.getmodule(inspect.stack()[0])._filesbymodname["__main__"]:
    import rungame

class AI:
    def __init__(self):
        print(__name__ + " AI Loaded")
        self.image = "tankblue3.png"

    def turn(self):

        #Start from here.
        enemy = self.robot.findClosestEnemy()
        dir = self.robot.getDirection(enemy)
        dis = self.robot.getDistance(enemy)
        print("dir:", dir)
        print("Robot x:", self.robot.x())
        print("distance:", dis)

        if self.robot.health < 50:
            self.robot.repair(self.robot.energy)
        elif dis < 50:
            self.robot.fireProjectile(dir)

        elif self.robot.x() >= 500 and self.robot.direction > -180:
            self.robot.turnRight(10)
        else:
            self.robot.moveForward(5)