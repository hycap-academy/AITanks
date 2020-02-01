import inspect
if "rungame" not in inspect.getmodule(inspect.stack()[0])._filesbymodname["__main__"]:
    import rungame

class AI:
    def __init__(self):
        print(__name__ + " AI Loaded")
        self.image = "tankred1.png"

    def turn(self):
        

        enemy = self.robot.findClosestEnemy()
        dis = self.robot.getDistance(enemy)
        if enemy != None:
            if self.robot.energy > 50:
                self.robot.dropBomb(enemy)
                self.robot.moveForward(10)
            