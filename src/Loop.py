'''
Created on Dec 19, 2016

@author: Trayvon
'''
import time
from threading import Thread
from ShutDown import shutdown
from StartUp import startUp
from Update import update
from Draw import draw

#This file will contain the main components of the loop
class GameLoop:
    runFlag = False
    
    #Start the game loop
    def run(self, delta):
        runFlag = True
        
        startUp()
        
        #convert time to seconds
        nextTime = time.time() + 60
        maxTimeDiff = 0.5
        skippedFrames = 1
        maxSkippedFrames = 5
        
        while(runFlag):
            currTime = time.time() / 1000000000.0
            if((currTime - nextTime) > maxTimeDiff):
                nextTime = currTime
            if(currTime >= nextTime):
                #new time for update
                nextTime += delta
                update()
                
                if((currTime < nextTime) | (skippedFrames > maxSkippedFrames)):
                    draw()
                    skippedFrames = 1
                else:
                    skippedFrames + 1
            else:
                #determine sleep time
                sleepTime = 1000.0 * (nextTime - currTime)
                if(sleepTime > 0):
                    #sleep until next update
                    try:
                        time.sleep(sleepTime)
                    except InterruptedError:
                        #do nothing
    
        #inside of run
        shutdown()
        
    def stop(self):
        runFlag = False
        
    startUp()
    shutdown()
    update()
    draw()
                        
                    
    
    