"""Mòdul d'exemple per a la demo de Read the Docs."""


def suma(a, b):
    """Suma dos nombres.

    Args:
        a (float): Primer nombre.
        b (float): Segon nombre.

    Returns:
        float: La suma de ``a`` i ``b``.
    """
    return a + b


def factorial(n):
    """Calcula el factorial de ``n`` de forma recursiva.

    Args:
        n (int): Nombre enter no negatiu.

    Returns:
        int: ``n!``

    Raises:
        ValueError: Si ``n`` és negatiu.
    """
    if n < 0:
        raise ValueError("n ha de ser no negatiu")
    return 1 if n <= 1 else n * factorial(n - 1)
