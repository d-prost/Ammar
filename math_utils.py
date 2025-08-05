"""Utility mathematical functions."""

def factorial(n: int) -> int:
    """Return the factorial of ``n``.

    Parameters
    ----------
    n: int
        Non-negative integer.

    Returns
    -------
    int
        ``n!``.

    Raises
    ------
    ValueError
        If ``n`` is negative.
    """
    if n < 0:
        raise ValueError("n must be non-negative")

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
