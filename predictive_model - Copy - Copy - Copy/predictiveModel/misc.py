import random
from .linearRegression import *

class misc:
    def data(self, currentSpeed, totalFuelUsed, rpm, totalDistance, wheelSpeed, engineTemp, engineLoad, engineHours):
        currentSpeed = currentSpeed+3
        totalFuelUsed = totalFuelUsed+1
        rpm = rpm-7
        totalDistance = totalDistance+1
        wheelSpeed = wheelSpeed+3
        engineTemp= engineTemp
        engineLoad= engineLoad
        engineHours= engineHours
        nextMaintenance = linearRegressionModel(currentSpeed, totalFuelUsed, rpm, totalDistance, wheelSpeed, engineTemp,
                                                engineLoad, engineHours)
        return currentSpeed, totalFuelUsed, rpm, totalDistance, wheelSpeed, engineTemp, engineLoad, engineHours, nextMaintenance
