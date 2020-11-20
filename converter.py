import json
import numpy as np 
import sqlite3
import io

data = []
def load_tester(path):
    with open(path) as f:
        data.append(json.load(f))
    return np.asarray(data[0])

