import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler

data = pd.read_json("./samFavoriteData.json")
def create_dataset(dataset, time_step=15):
    dataX = [];
    for i in range(len(dataset)-time_step-1):
        a = dataset[i:(i+time_step)]   ###i=0, 0,1,2,3-----99   100 
        dataX.append(a)
    return np.array(dataX)

def data_processing(data_array, scaler):
    New_data=scaler.fit_transform(np.array(data_array).reshape(-1,1))
    new_data_set = create_dataset(New_data)
    return new_data_set

def corn(address, data_array):
    model = tf.keras.models.load_model(address, compile=False)
    scaler=MinMaxScaler(feature_range=(0,1))
    Processed_data = data_processing(data_array, scaler)
    pred = model.predict(Processed_data)
    train_predict = scaler.inverse_transform(pred)
    return train_predict[-1]
price_for_tmr = corn("./lstm.h5", np.array(data["close"]))   
