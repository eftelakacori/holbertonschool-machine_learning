import math

class Poisson:
    """Përfaqëson një shpërndarje Poisson."""

    def __init__(self, data=None, lambtha=1.):
        """Inicializon shpërndarjen Poisson."""
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha duhet të jetë një vlerë pozitive")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data duhet të jetë një listë")
            if len(data) < 2:
                raise ValueError("data duhet të përmbajë disa vlera")
            self.lambtha = float(sum(data) / len(data))

    def pmf(self, k):
        """
        Llogarit funksionin e masës së probabilitetit (PMF) për një numër të caktuar suksesesh.

        Args:
            k (int): Numri i suksesesh.

        Returns:
            float: Vlera e PMF për k.
        """
        if not isinstance(k, (int, float)):
            return 0
        k = int(k)  # Konverto k në integer
        if k < 0:
            return 0
        return (math.exp(-self.lambtha) * self.lambtha ** k) / math.factorial(k)
