#!/usr/bin/env python3
"""defines function that returns the transpose of a 2D matrix"""


def add_arrays(arr1, arr2):
    """
    Adds two arrays element-wise.
    
    Args:
        arr1 (list): The first array (list of ints/floats).
        arr2 (list): The second array (list of ints/floats).
    
    Returns:
        list: A new list containing the element-wise sum of arr1 and arr2,
              or None if the arrays have different shapes.
    """
    # Kontrollo nëse listat kanë të njëjtën gjatësi
    if len(arr1) != len(arr2):
        return None
    # Kthe listën që është shuma element-për-element
    return [arr1[i] + arr2[i] for i in range(len(arr1))]
