#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import mysql.connector as mariadb
import numpy as np
import random
from scipy import signal


def distance(a, q, c):
    return sum(((a[d][q] - a[d][c]) ** 2) for d in range(8)) ** 0.5


if __name__ == '__main__':
    cnx = mariadb.connect(user='root', host='localhost', database='dm', charset='utf8')
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM Power")
    ns, nu, cs, cu, ss, su, es, eu = [], [], [], [], [], [], [], []
    for (
        updateTime, northSupply, northUsage, centerSupply, centerUsage,
        southSupply, southUsage, eastSupply, eastUsage
    ) in cursor:
        ns.append(northSupply)
        nu.append(northUsage)
        cs.append(centerSupply)
        cu.append(centerUsage)
        ss.append(southSupply)
        su.append(southUsage)
        es.append(eastSupply)
        eu.append(eastUsage)
    idx1, idx2 = random.randrange(0, len(ns)), random.randrange(0, len(ns))
    print('Choose record #', idx1, ' as Q and record #', idx2, ' as C.', sep='', flush=True)
    arr = np.array([ns, nu, cs, cu, ss, su, es, eu])
    print('Before transformation: D(Q,C) =', distance(arr, idx1, idx2), flush=True)
    mean = np.mean(arr, axis=1)
    i = 0
    result = []
    for item in [ns, nu, cs, cu, ss, su, es, eu]:
        result.append(list(map(lambda x: x - mean[i], item)))
        i += 1
    print('After offset translation: D(Q,C) =', distance(result, idx1, idx2), flush=True)
    std = np.std(arr, axis=1)
    i = 0
    result = []
    for item in [ns, nu, cs, cu, ss, su, es, eu]:
        result.append(list(map(lambda x: (x - mean[i]) / std[i], item)))
        i += 1
    print('After amplitude scaling: D(Q,C) =', distance(result, idx1, idx2), flush=True)
    detrend = signal.detrend(arr, axis=1)
    print('After linear trend removal: D(Q,C) =', distance(detrend, idx1, idx2), flush=True)
    smooth = signal.savgol_filter(arr, 5, 2, axis=1)
    print('After noise reduction: D(Q,C) =', distance(smooth, idx1, idx2), flush=True)
    cursor.close()
    cnx.close()
