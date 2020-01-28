import inspect
if "rungame" not in inspect.getmodule(inspect.stack()[0])._filesbymodname["__main__"]:
    import rungame

class AI:
    def __init__(self):
        print(__name__ + " AI Loaded")
        self.image = "tankblue2.png"

    def turn(self):
        

        enemy = self.robot.findClosestEnemy()
        dis = self.robot.getDistance(enemy)
        print ("movingbomb: dir, x, y:", self.robot.direction, self.robot.x(), self.robot.y())
        if enemy != None:
            dir = self.robot.getDirection(enemy)
            self.robot.dropBomb(enemy)
            if self.robot.x() <=20 and self.robot.direction > -90:
                self.robot.turnRight(5)
            elif  self.robot.x() > 540 and self.robot.direction < 90:
                self.robot.turnLeft(5)
            else:
                self.robot.moveForward(5)

            