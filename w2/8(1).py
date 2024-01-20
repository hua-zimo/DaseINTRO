import random
import numpy as np

def throwNeedles(num):
    inCircle = 0
    for i in range(1, num+1):
        x = random.random()
        y = random.random()
        if(x*x + y*y)**0.5 <= 1: 
            inCircle += 1
           
    return 4*(inCircle/num)

def getEst(num, numTrials):
    est = []
    for t in range(numTrials):
        piGuess = throwNeedles(num)
        est.append(piGuess)
    
    curEst = sum(est)/len(est)
    sDev = np.std(est)
    
    return(curEst, sDev)

def estPi(precision, numTrials):
    num = 1000
    sDev = precision
    while sDev > precision/1.96 :
        curEst, sDev = getEst(num, numTrials)
        num *= 2
    
    return curEst

if __name__ == "__main__":
    print(estPi(0.01, 100))
    
#参考：教材
    