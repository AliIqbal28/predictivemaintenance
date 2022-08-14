import pandas as pd

from sklearn import linear_model


### SCALE TRAIN DATA ###
def scale(df):
    return (df - df.min()) / (df.max() - df.min())


def linearRegressionModel(Speed, total_fuel_used, rpm, odometer, wheel_speed, engine_temp, j1939_eng_load,
                          J1708_eng_hrs):
    df1 = pd.read_excel(r'C:\Users\aliiq\OneDrive\Desktop\predictive_model\predictiveModel\finalDatasetPrediction.xlsx')

    df2 = pd.DataFrame({"Speed": Speed,
                        "total_fuel_used": total_fuel_used,
                        "rpm": rpm,
                        "odometer": odometer,
                        "wheel_speed": wheel_speed,
                        "engine_temp": engine_temp,
                        "j1939_eng_load": j1939_eng_load,
                        "J1708_eng_hrs": J1708_eng_hrs
                        }, index=[0])

    df1Label = df1["next_maintenance"]
    del df1["next_maintenance"]

    ### drop columns with low standard deviation and variance
    df1 = df1.dropna(axis=1)
    df2 = df2.dropna(axis=1)
    x_train = df1
    y_train = df1Label
    ### fit the model
    lm = linear_model.LinearRegression()
    lm.fit(x_train, y_train)
    predictedNextMaintenance = int(lm.predict(df2))
    return predictedNextMaintenance
