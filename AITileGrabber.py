

import inspect
if "rungame" not in inspect.getmodule(inspect.stack()[0])._filesbymodname["__main__"]:
    import rungame

class AI:
    def __init__(self):
        print(__name__ + " AI Loaded")
        self.image = "tankred1.png"

    def turn(self):
        t = self.robot.findClosestNewTile()
        dir1 = self.robot.getDirection(t)
        dis1 = self.robot.getDistance(t)
        if dir1 > 3:
            self.robot.turnLeft(5)
        elif dir1 < -3:
            self.robot.turnRight(5)
        else:
            self.robot.moveForward(5)