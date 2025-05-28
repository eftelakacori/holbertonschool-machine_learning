#!/usr/bin/env python3
"""A function that performs back propagation over a
pooling layer of a neural network"""
import numpy as np


def pool_backward(dA, A_prev, kernel_shape, stride=(1, 1), mode='max'):
    """A function that performs back propagation over a pooling layer
    of a neural network"""
    m, h_new, w_new, c = dA.shape
    m, h_prev, w_prev, _ = A_prev.shape
    kh, kw = kernel_shape
    sh, sw = stride

    dA_prev = np.zeros_like(A_prev)

    for i in range(m):
        for h in range(h_new):
            for w in range(w_new):
                for ch in range(c):
                    vert_start = h * sh
                    vert_end = vert_start + kh
                    h_start = w * sw
                    h_end = h_start + kw

                    if mode == 'max':
                        mask = A_prev[i, vert_start:vert_end,
                                      h_start:h_end,
                                      ch] == np.max(A_prev[i,
                                                           vert_start:vert_end,
                                                           h_start:h_end,
                                                           ch])
                        dA_prev[i, vert_start:vert_end, h_start:h_end,
                                ch] += mask * dA[i, h, w, ch]
                    elif mode == 'avg':
                        avg = np.mean(A_prev[i, vert_start:vert_end,
                                             h_start:h_end, ch])
                        dA_prev[i, vert_start:vert_end, h_start:h_end,
                                ch] += np.ones((kh, kw)) * dA[i, h, w,
                                                              ch] / (kh * kw)

    return dA_prev
