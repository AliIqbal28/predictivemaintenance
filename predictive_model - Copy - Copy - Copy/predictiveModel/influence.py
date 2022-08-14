import matplotlib.pyplot as plt

plt.style.use('ggplot')
import pandas as pd
from sklearn import linear_model
from .influenceObject import *

list_Predictions = []
influenceDetailObjects = []


# find object with same uuid
def findObj(uuid):
    for obj in list_Predictions:
        if int(obj.UUID) == int(uuid):
            return obj


def calculateInfluence(uuid):
    influenceObj = findObj(uuid)
    df1 = pd.read_excel(r'C:\Users\aliiq\OneDrive\Desktop\predictive_model\predictiveModel\finalDatasetPrediction.xlsx')
    df2 = pd.DataFrame({"Speed": influenceObj.currentSpeed,
                        "total_fuel_used": influenceObj.totalFuelUsed,
                        "rpm": influenceObj.rpm,
                        "odometer": influenceObj.totalDistance,
                        "wheel_speed": influenceObj.wheelSpeed,
                        "engine_temp": influenceObj.engineTemp,
                        "j1939_eng_load": influenceObj.engineLoad,
                        "J1708_eng_hrs": influenceObj.engineHours
                        }, index=[0])
    df1Label = df1["next_maintenance"]
    del df1["next_maintenance"]
    x_train = df1
    y_train = df1Label
    linreg = linear_model.LinearRegression()
    linreg.fit(x_train, y_train)
    importance = linreg.coef_
    # summarize feature importance
    for i, v in enumerate(importance):
        if i == 0:
            featureName = "Current Speed"
        if i == 1:
            featureName = "Total fuel used"
        if i == 2:
            featureName = "rpm"
        if i == 3:
            featureName = "Total Distance"
        if i == 4:
            featureName = "Wheel Speed"
        if i == 5:
            featureName = "Engine Temperature"
        if i == 6:
            featureName = "Engine Load"
        if i == 7:
            featureName = "Engine Hours"
        score = f"{abs(int(v))}"
        influenceDetailObjects.append(influenceDetail(featureName, score))

    results = [obj.to_dict() for obj in influenceDetailObjects]
    influenceDetailObjects.clear()
    return results
