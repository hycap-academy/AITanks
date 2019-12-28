import inspect
if "rungame" not in inspect.getmodule(inspect.stack()[0])._filesbymodname["__main__"]:
    import rungame

class AI:
    def __init__(self):
        print(__name__ + " AI Loaded")
        self.image = "DozerRed.png"

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
            elif dis <= 225:
                self.robot.fireProjectile(dir)
            elif dis > 225:
                self.robot.moveForward(10)

            