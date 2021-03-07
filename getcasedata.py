import pandas as pd
import numpy as np
import tensorflow as tf

def get_data(normalize):
    data = pd.read_csv("covid-19-data/us-states.csv")
    states = data["state"].unique()
    ret = {}
    a = np.array([], dtype=np.float32)
    for state in states:
        result = np.diff(np.append(np.array([0], dtype=np.float32), data[data["state"] == state][data["date"] >= "2020-03-01"]["cases"].to_numpy(dtype=np.float32)))
        # result = np.convolve(result, np.ones(7), "valid") / 7
        ret[state] = result
        a = np.concatenate((a, result))
    m = max(0, np.amin(a))
    s = np.amax(a)
    print(m)
    print(s)
    if normalize:
        for k in ret.keys():
            d = ret[k]
            ret[k] = (np.clip(d, 0, None) - (m + s) / 2) / (s - m) * 2
    return ret

def get_window(data):
    return tf.keras.preprocessing.timeseries_dataset_from_array(
      data=data,
      targets=None,
      sequence_length=28,
      sequence_stride=1,
      shuffle=True,
      batch_size=16,)
