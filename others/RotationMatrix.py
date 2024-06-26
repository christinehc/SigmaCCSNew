# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 10:31:23 2023

@author: yxliao
"""

import numpy as np
from sklearn.metrics import r2_score

def Rx(theta):
    R_x = np.array([
        [1, 0, 0],
        [0, np.cos(theta), -np.sin(theta)],
        [0, np.sin(theta),  np.cos(theta)],
    ])
    return R_x

def Ry(theta):
    R_y = np.array([
        [np.cos(theta), 0, np.sin(theta)],
        [0, 1, 0],
        [-np.sin(theta), 0, np.cos(theta)],
    ])
    return R_y

def Rz(theta):
    R_z = np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta), np.cos(theta), 0],
        [0, 0, 1],
    ])
    return R_z

