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

            self.robot.direction = self.robot.normalizeDir(self.robot.direction)
            print (self.robot.direction)
            if self.robot.energy >=75 and self.robot.shield==False:
                self.robot.shieldOn()
            else:
                if dis < 300:
                    if self.robot.x() <=10 and self.robot.y() > 530 and self.robot.direction>0:
                        self.robot.turnRight(10)
                    elif self.robot.x() <=20 and self.robot.y() <=10 and self.robot.direction > -90:
                        self.robot.turnRight(10)
                    elif  self.robot.x() > 540  and self.robot.y() < 20 and self.robot.direction > -180:
                        self.robot.turnRight(10)
                    elif self.robot.x() > 530 and self.robot.y() > 530  and (self.robot.direction > 90 or self.robot.direction== -180):
                        self.robot.turnRight(10)
                    else:
                        self.robot.moveForward(10)

            if self.robot.energy > 50:
                self.robot.fireProjectile(dir)
