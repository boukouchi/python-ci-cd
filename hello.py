"""
Programme qui réalise une permutation circulaire de trois nombres.

Après la permutation :
a prend la valeur de b
b prend la valeur de c
c prend la valeur de a
"""


def permutation(n1, n2, n3):
    """
    Effectue une permutation circulaire de trois nombres.

    Args:
        a (int): Premier nombre.
        b (int): Deuxième nombre.
        c (int): Troisième nombre.

    Returns:
        tuple: Les trois nombres après permutation.
    """
    return n2, n3, n1

print("Hello")
# Programme principal
a = 10
b = 30
c = 90

print(f"\nAvant permutation : a={a}, b={b}, c={c}")

a, b, c = permutation(a, b, c)

print(f"Après permutation : a={a}, b={b}, c={c}")
