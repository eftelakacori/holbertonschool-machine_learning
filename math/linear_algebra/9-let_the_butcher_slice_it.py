



def add_matrices2D(mat1, mat2):
    """
    Adds two 2D matrices element-wise.

    Args:
        mat1: First 2D matrix (list of lists containing ints/floats).
        mat2: Second 2D matrix (list of lists containing ints/floats).

    Returns:
        A new 2D matrix with the element-wise sum, or None if the matrices are not the same shape.
    """
    # Check if the matrices have the same shape
    if len(mat1) != len(mat2) or any(len(row1) != len(row2) for row1, row2 in zip(mat1, mat2)):
        return None

    # Perform element-wise addition
    return [[mat1[row][col] + mat2[row][col] for col in range(len(mat1[row]))] for row in range(len(mat1))]

