import time



class PID:
    def _init_(self, kp , kd , ki , maxVel,  setPtVel):
        self.Kp = kp
        self.Kd = kd
        self.Ki = ki
        self.maxVel = maxVel
        self.setPtVel = setPtVel
        self.intEHead = 0
        self.prevEHead = 0
        self.prevTime = time.time()

    def changeGain(self,newKp , newKd , newKi):
            self.Kp = newKp
            self.Kd = newKd
            self.Ki = newKi

    def calculate(self):
        
        tdelta = time.time() - self.prevTime
        EHead = self.setPtHead - self.currHead
        intEHead += intEHead + EHead*self.tdelta
        diffEHead = (EHead - self.prevEHead )/self.tdelta
        uHead = self.Kp*EHead + self.Kd*diffEHead + self.Ki*intEHead
        if( uHead > self.maxVel):
            uHead = self.maxVel
        elif (uHead < -self.maxVel):
            uHead = -self.maxVel
        self.prevEHead = EHead
        prevTime = time.time()