#!/usr/bin/env python3
"""That performs PCA on a dataset"""


def pca(X, var=0.95):
    """
    Parametrat:
    - X: numpy.ndarray me formë (n, d), ku n është
    numri i pikave të të dhënave
      dhe d është numri i tipareve.
    - var: float, pjesa e variancës që do të ruhet.

    Kthen:
    - W: numpy.ndarray me formë (d, nd), matrica
     e pesheve që projeksion të të dhënave
      në hapësirën e re me dimensione të zvogëluara.
    """

    # Hapi 1: Llogaritja e matricës së kovariancës
    cov_matrix = np.cov(X.T)

    """Hapi 2: Llogaritja e eigenvlerave dhe 
    eigenvektorëve të matricës së kovariancës"""
    eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)

    """Hapi 3: Renditja e eigenvlerave në rend
    descending dhe përzgjedhja e eigenvektorëve përkatës"""
    
    sorted_indices = np.argsort(eigenvalues)[::-1]
    eigenvalues = eigenvalues[sorted_indices]
    eigenvectors = eigenvectors[:, sorted_indices]

    # Hapi 4: Llogaritja e variancës kumulative
    total_variance = np.sum(eigenvalues)
    cumulative_variance = np.cumsum(eigenvalues) / total_variance

    # Debugging: Shiko sa komponentë po përzgjidhen dhe sa variancë po ruhet
    print(f"Varianca totale: {total_variance}")
    print(f"Varianca kumulative: {cumulative_variance}")
    
    # Hapi 5: Zgjedh numrin e komponentëve që ruajnë variancën e kërkuar
    nd = np.where(cumulative_variance >= var)[0][0] + 1

    print(f"Komponentët e përzgjedhur: {nd}")

    # Hapi 6: Zgjedh eigenvektorët përkatës (komponentët kryesorë)
    W = eigenvectors[:, :nd]

    return W
