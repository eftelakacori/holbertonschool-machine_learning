#!/usr/bin/env python3
"""defines function that performs matrix multiplication"""


def mat_mul(mat1, mat2):
    # Kontrolloni nëse matrica mund të shumëzohen
    if len(mat1[0]) != len(mat2):
        return None

    # Gjej dimensionet e matricave
    rows_mat1 = len(mat1)
    cols_mat1 = len(mat1[0])
    cols_mat2 = len(mat2[0])

    # Krijoni një matrice bosh për të ruajtur rezultatin
    result = [[0 for _ in range(cols_mat2)] for _ in range(rows_mat1)]

    # Kryeni shumëzimin e matricave
    for i in range(rows_mat1):
        for j in range(cols_mat2):
            for k in range(cols_mat1):
                result[i][j] += mat1[i][k] * mat2[k][j]

    return result
