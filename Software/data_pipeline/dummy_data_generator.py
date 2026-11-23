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
import random

# %%
ELECTRODES = ['Fp1', 'Fp2', 'C3', 'C4', 'P7', 'P8', 'O1', 'O2']
BANDS = ['delta', 'theta', 'alpha', 'beta', 'gamma']
CHANNELS = [f"{e}_{b}" for e in ELECTRODES for b in BANDS]
LABELS = ['close_right', 'close_left', 'open_right', 'open_left']


# %%
def generate_data(length):
    """Returns a pandas dataframe with 41 columns and the specified length of rows."""
    df = pd.DataFrame(np.random.rand(length, 40), 
                      columns = CHANNELS)
    #generate labels
    labels_list = []
    while len(labels_list) < length:
        times = min(random.randint(100, 150), length - len(labels_list))
        labels_list.extend([LABELS[random.randint(0, len(LABELS) - 1)]] * times)
    df['labels'] = labels_list
    return df

# %%
#df = generate_data(10000)
#df.to_csv('dummy_data.csv', index = False)

# %%
