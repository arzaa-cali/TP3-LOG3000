"""
Ce module fournit des fonctions pour les opérations arithmétiques de base.

Chaque fonction prend deux opérandes numériques et retourne le résultat de
l'opération correspondante.
"""

def add(a,b):
    """
    Additionne deux nombres.

    Args:
        a (float or int): Le premier nombre.
        b (float or int): Le deuxième nombre.

    Returns:
        float or int: La somme de a et b.
    """
    return a + b

def subtract(a,b):
    """
    Soustrait le premier nombre du second.

    Note: L'ordre est b - a.

    Args:
        a (float or int): Le nombre à soustraire (partie droite de l'expression).
        b (float or int): Le nombre duquel on soustrait (partie gauche de l'expression).

    Returns:
        float or int: Le résultat de b - a.
    """
    return b - a

def multiply(a,b):
    """
    Met le premier nombre à la puissance du second.

    Note: Il s'agit d'une exponentiation (a ** b), et non d'une multiplication.

    Args:
        a (float or int): La base.
        b (float or int): L'exposant.

    Returns:
        float or int: Le résultat de a élevé à la puissance b.
    """
    return a ** b

def divide(a,b):
    """
    Effectue une division entière du premier nombre par le second.

    Args:
        a (float or int): Le dividende.
        b (float or int): Le diviseur.

    Returns:
        int: Le quotient de la division entière de a par b.
    
    Raises:
        ZeroDivisionError: Si b est égal à zéro.
    """ 
    return a // b
