import numpy as np
from tqdm import tqdm

"""
This part corresponds to the different useful fonctions for the pre-processing.
This part is inpired by Deep-Trading github.
Thanks to this amazing git : https://github.com/Rachnog/Deep-Trading for this set of functions.

"""


def shuffle_in_unison(a, b, seed = 42):
    # courtsey http://stackoverflow.com/users/190280/josh-bleecher-snyder

    np.random.seed(seed)
    assert len(a) == len(b)
    shuffled_a = np.empty(a.shape, dtype=a.dtype)
    shuffled_b = np.empty(b.shape, dtype=b.dtype)
    permutation = np.random.permutation(len(a))
    for old_index, new_index in enumerate(permutation):
        shuffled_a[new_index] = a[old_index]
        shuffled_b[new_index] = b[old_index]
    return shuffled_a, shuffled_b
 
 
def create_Xt_Yt(X, y, percentage_train=0.8, percentage_val = 0.1, percentage_test = 0.1):
    p_train = int(len(X) * percentage_train)
    p_val = int(len(X) * percentage_val)
    p_test = int(len(X) * percentage_test)


    X_train = X[0:p_train]
    Y_train = y[0:p_train]
     
    X_train, Y_train = shuffle_in_unison(X_train, Y_train)
 
    X_val = X[p_train:p_train+p_val]
    Y_val = y[p_train:p_train+p_val]

    X_test = X[p_train+p_val:]
    Y_test = y[p_train+p_val:]


    return X_train, X_test, X_val, Y_train, Y_val, Y_test


def remove_nan_examples(data):
    newX = []
    for i in range(len(data)):
        if np.isnan(data[i]).any() == False:
            newX.append(data[i])
    return newX



def get_X_Y(df, WINDOW = 30, EMB_SIZE = 5, STEP = 1, FORECAST = 1):
    openp = df.loc[:, 'open'].tolist()
    highp = df.loc[:, 'high'].tolist()
    lowp = df.loc[:, 'low'].tolist()
    closep = df.loc[:, 'close'].tolist()
    volumep = df.loc[:, 'volume'].tolist()
     
    X, Y = [], []
    for i in range(0, len(df), STEP): 
        try:
            o = openp[i:i+WINDOW]
            h = highp[i:i+WINDOW]
            l = lowp[i:i+WINDOW]
            c = closep[i:i+WINDOW]
            v = volumep[i:i+WINDOW]

            o = (np.array(o) - np.mean(o)) / np.std(o)
            h = (np.array(h) - np.mean(h)) / np.std(h)
            l = (np.array(l) - np.mean(l)) / np.std(l)
            c = (np.array(c) - np.mean(c)) / np.std(c)
            v = (np.array(v) - np.mean(v)) / np.std(v)

            x_i = closep[i:i+WINDOW]
            y_i = closep[i+WINDOW+FORECAST]  

            last_close = x_i[-1]
            next_close = y_i

            if last_close < next_close:
                y_i = 0
            else:
                y_i = 1

            x_i = np.column_stack((o, h, l, c, v))

        except Exception as e:
            break
        X.append(x_i)
        Y.append(y_i)
    return X, Y

