import inspect
if "rungame" not in inspect.getmodule(inspect.stack()[0])._filesbymodname["__main__"]:
    import rungame

class AI:
    def __init__(self):
        print(__name__ + " AI Loaded")
        self.image = "tankblue1.png"

    def turn(self):
        

        enemy = self.robot.findClosestEnemy()
        dis = self.robot.getDistance(enemy)
        if enemy != None:
            dir = self.robot.getDirection(enemy)
            print ("runandshoot: dir, x, y:", self.robot.direction, self.robot.x(), self.robot.y())
            if self.robot.energy >=75 and self.robot.shield==False:
                self.robot.shieldOn()
            else:
                if dis < 250:
                    if self.robot.x() <=20 and self.robot.y() > 530 and self.robot.direction>0:
                        self.robot.turnRight(10)
                    elif self.robot.x() <=20 and self.robot.y() <=10 and self.robot.direction > -90:
                        self.robot.turnRight(10)
                    elif  self.robot.x() > 540  and self.robot.y() < 60 and self.robot.direction > -180:
                        self.robot.turnRight(10)
                    elif self.robot.x() > 530 and self.robot.y() > 530  and (self.robot.direction > 90 or self.robot.direction== -180):
                        self.robot.turnRight(10)
                    else:
                        if dis < 100:
                            self.robot.moveForward(8)

            if self.robot.energy > 50:
                if dis < 250:
                    self.robot.fireProjectile(dir)
                else:
                    self.robot.dropBomb(enemy)