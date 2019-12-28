import inspect
if "rungame" not in inspect.getmodule(inspect.stack()[0])._filesbymodname["__main__"]:
    import rungame

class AI:
    def __init__(self):
        print(__name__ + " AI Loaded")
        self.image = "DozerRed.png"

    def turn(self):
        

        enemy = self.robot.findClosestEnemy()
        dis = self.robot.getDistance(enemy)
        if enemy != None:
            dir = self.robot.getDirection(enemy)
            self.robot.fireProjectile(dir)
            