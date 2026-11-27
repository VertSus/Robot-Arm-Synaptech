# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.7
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import numpy as np
import pandas as pd
import math

# %%
""" Splits the input array(data) into smaller arrays of the specified window_size, starting at 
0 and every subsequent nth index(step_size), excluding the last column, and adds them to a new 
numpy array. Creates a new numpy array containing each nth(step_size) label. 
Returns both new arrays in a tuple.
"""
def sliding_windows(data, window_size, step_size): #baseline window_size 50, step_size 25

    length = data.shape[0] // step_size -1
    
    windows = np.empty((length, window_size, data.shape[1]-1), dtype = np.float32)
    labels = np.empty(length, dtype = object)

    for i in range(0, data.shape[0] - window_size + 1, step_size):
        windows[i//step_size] = data[i:i + window_size, 0:data.shape[1] - 1]
        labels[i//step_size] = data[i + window_size - 1, data.shape[1] - 1]
        
    return (np.array(windows), np.array(labels))
    


# %%
arr = pd.read_csv('dummy_data.csv').to_numpy()

# %%
windows, labels = sliding_windows(arr, 50, 25)

# %%
print(windows[0])
print(labels[0])

# %%
