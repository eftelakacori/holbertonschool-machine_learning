#!/usr/bin/env python3

def mat_mul(mat1, mat2):
    """
    Shumëzon dy matrica mat1 dhe mat2.

    Parametra:
    mat1 (listë e listave të int-eve/floateve): Matrica e parë për të shumëzuar.
    mat2 (listë e listave të int-eve/floateve): Matrica e dytë për të shumëzuar.

    Kthen:
    listë e listave të int-eve/floateve: Një matricë të re që përfaqëson rezultatin e shumimit të matricave.
    Nëse matricat nuk mund të shumëzohen (për shkak të dimensioneve jo përputhëse), kthen None.
    """
    # Kontrollo nëse numri i kolonave në mat1 është i barabartë me numrin e rreshtave në mat2
    if len(mat1[0]) != len(mat2):
        return None

    # Inicjalizo një matricë rezultati me dimensionet përkatëse (rreshtat e mat1 x kolonat e mat2)
    result = [[0 for _ in range(len(mat2[0]))] for _ in range(len(mat1))]

    # Kryej shumëzimin e matricave
    for i in range(len(mat1)):  # Kalo përmes rreshtave të mat1
        for j in range(len(mat2[0])):  # Kalo përmes kolonave të mat2
            for k in range(len(mat2)):  # Kalo përmes kolonave të mat1 (rreshtave të mat2)
                result[i][j] += mat1[i][k] * mat2[k][j]

    return result

# Testimi i rastit
mat1 = [[1, 2],
        [3, 4],
        [5, 6]]
mat2 = [[1, 2, 3, 4],
        [5, 6, 7, 8]]

print(mat_mul(mat1, mat2))
