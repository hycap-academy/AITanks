
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
        

        if dir > 0:
            self.robot.turnRight(5)
        elif dir < 0:
            self.robot.turnLeft(5)
            