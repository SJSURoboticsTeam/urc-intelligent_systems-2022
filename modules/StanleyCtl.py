import time
import math
from MPU6050 import MPU6050


class Stanley:
    def _init_(self, k , ks  , maxSteer,  steerError, crossTrackError):
        self.K = k
        self.Ks = ks
        self.maxSteer = maxSteer
        self.prevTime = time.time()
        self.steerError = steerError
        self.xtrackError = crossTrackError
        self.prevTime = time.time()

    def changeGain(self,newK , newKs):
        self.K = newK
        self.Ks = newKs

    def calculate(self):
        
        tdelta = time.time() - self.prevTime
        mpu = MPU6050()
        mpu.read_data
        dt = time.time() - prevTime
        
        velX = mpu.ACCEL_XOUT_H/dt
        velY = mpu.ACCEL_YOUT_H/dt
        velF = math.sqrt(velX^2 + velY^2)
        velocity = mpu.ACCEL_ZOUT_H/dt 
        final_angle = self.steerError + math.atan2(self.K*self.crossTrackError,self.Ks+velF)
        if( final_angle > self.maxSteer):
            final_angle = self.maxSteer
        elif (final_angle < -self.maxSteer):
            final_angle = -self.maxSteer
        prevTime = time.time()