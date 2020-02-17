import inspect
if "rungame" not in inspect.getmodule(inspect.stack()[0])._filesbymodname["__main__"]:
    import rungame

class AI:
    def __init__(self):
        print(__name__ + " AI Loaded")
        self.image = "tankblue4.png"

    def turn(self):
        print("Do Nothing")
        #t = self.robot.findClosestNewTile()
        #dir = self.robot.getDirection(t)
        #dis = self.robot.getDistance(t)
        #print(dir, dis)
            