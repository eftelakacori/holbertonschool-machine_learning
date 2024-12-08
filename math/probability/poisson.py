import math

class Poisson:
    """Represents a Poisson distribution."""

    def __init__(self, data=None, lambtha=1.):
        """Initialize a Poisson distribution."""
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = float(sum(data) / len(data))

    def pmf(self, k):
        """
        Calculate the Probability Mass Function (PMF) for a given number of successes.
        
        Args:
            k (int): The number of successes.
        
        Returns:
            float: The PMF value for k.
        """
        if not isinstance(k, (int, float)):
            return 0
        k = int(k)
        if k < 0:
            return 0
        return (math.exp(-self.lambtha) * self.lambtha ** k) / math.factorial(k)
