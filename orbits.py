import matplotlib.pyplot as plt
import numpy as np

#constants and body container
constG = 6.67 * (10**-1) #Real G = 6.67 * (10**-11)
bodys = np.array([])
bodyCount = 3
plt.title('Orbits')

#distance between two xy vecter
def vecDistance(vec1, vec2):
    return ((vec2[0] - vec1[0])**2 + (vec2[1] - vec1[1])**2)**0.5

#unit components
def vecComponent(vec1, vec2):
    theta = np.arctan((vec2[1]-vec1[1]) / (vec2[0] - vec1[0]))
    if vec2[0] < vec1[0]: theta += np.pi

    return np.array([np.cos(theta), np.sin(theta)])
    
#Orbiting Body Property
class body:
    def __init__(self, mass, pos, vel):
        self.m = mass
        self.pos = pos
        self.vel = vel
    
    def updateVel(self):
        for mainSat in bodys:
            for compSat in bodys:
                if compSat == mainSat: continue
                accMag = constG * compSat.m / ((vecDistance(mainSat.pos, compSat.pos))**2)
                mainSat.vel = np.add(mainSat.vel, accMag*vecComponent(mainSat.pos, compSat.pos))
    
    def updatePos(self):
        for mainSat in bodys: mainSat.pos = np.add(mainSat.pos, mainSat.vel)
            
#Procedural bodys init
for i in range(bodyCount):
    bodys = np.append(bodys, body(35, [-200/(bodyCount+1) + i * 200/(bodyCount+1), -200/(bodyCount+1) + i * 200/(bodyCount+1)], [0.4 + -0.4*i, 0]))

while True:
    plotX, plotY = np.array([]), np.array([])
    for aBody in bodys: aBody.updateVel()
    for aBody in bodys:
        aBody.updatePos()
        plotX, plotY = np.append(plotX, aBody.pos[0]), np.append(plotY, aBody.pos[1])

    plt.plot(plotX, plotY, 'b.')
    plt.pause(0.05)