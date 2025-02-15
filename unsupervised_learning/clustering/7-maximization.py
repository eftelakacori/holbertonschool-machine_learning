import numpy as np

def kmeans(X, k, iterations=1000):
    """
    Performs K-means clustering on a dataset.
    
    Parameters:
    X : numpy.ndarray of shape (n, d) - dataset
    k : int - number of clusters
    iterations : int - maximum number of iterations
    
    Returns:
    C : numpy.ndarray of shape (k, d) - centroid means for each cluster
    clss : numpy.ndarray of shape (n,) - index of the cluster each data point belongs to
    """
    if not isinstance(X, np.ndarray) or len(X.shape) != 2:
        return None, None
    if not isinstance(k, int) or k <= 0 or k > X.shape[0]:
        return None, None
    if not isinstance(iterations, int) or iterations <= 0:
        return None, None
    
    n, d = X.shape
    
    # Initialize centroids using a multivariate uniform distribution
    min_vals = np.min(X, axis=0)
    max_vals = np.max(X, axis=0)
    C = np.random.uniform(min_vals, max_vals, size=(k, d))
    
    for _ in range(iterations):
        # Compute distances and assign each point to the closest centroid
        distances = np.linalg.norm(X[:, np.newaxis] - C, axis=2)
        clss = np.argmin(distances, axis=1)
        
        new_C = np.copy(C)
        
        for i in range(k):
            cluster_points = X[clss == i]
            if cluster_points.shape[0] == 0:
                # Reinitialize centroid if no points are assigned to it
                new_C[i] = np.random.uniform(min_vals, max_vals, size=(1, d))
            else:
                new_C[i] = np.mean(cluster_points, axis=0)
        
        # Check for convergence
        if np.all(C == new_C):
            break
        
        C = new_C
    
    return C, clss
