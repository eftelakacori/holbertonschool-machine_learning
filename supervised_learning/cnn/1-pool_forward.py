#!/usr/bin/env python3
"""A function that performs forward propagation
over a pooling layer of a neural network"""
import numpy as np


def pool_forward(A_prev, kernel_shape, stride=(1, 1), mode='max'):
    """A function that performs forward propagation over a pooling
    layer of a neural network"""
    m, h_prev, w_prev, c_prev = A_prev.shape
    kh, kw = kernel_shape
    sh, sw = stride

    out_h = int((h_prev - kh) / sh) + 1
    out_w = int((w_prev - kw) / sw) + 1

    Z = np.zeros((m, out_h, out_w, c_prev))

    for i in range(out_h):
        for j in range(out_w):
            h_start = i * sh
            h_end = h_start + kh
            w_start = j * sw
            w_end = w_start + kw

            a_slice_prev = A_prev[:, h_start:h_end, w_start:w_end, :]

            if mode == 'max':
                Z[:, i, j, :] = np.max(a_slice_prev, axis=(1, 2))
            elif mode == 'avg':
                Z[:, i, j, :] = np.mean(a_slice_prev, axis=(1, 2))

    return Z
