# -*- coding: utf-8 -*-
import paddle.v2 as paddle
import numpy as np
def train_reader():
    train_x = np.array([[1, 1], [1, 2], [3, 4], [5, 2]])
    train_y = np.array([-2, -3, -7, -7])

    def reader():
        for i in xrange(train_y.shape[0]):
            yield train_x[i], train_y[i]

    return reader
