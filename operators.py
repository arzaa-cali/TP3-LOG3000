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

    Args:
        a (float or int): Le nombre duquel on soustrait (partie gauche de l'expression).
        b (float or int): Le nombre à soustraire (partie droite de l'expression).
    Returns:
        float or int: Le résultat de a - b.
    """
    return b - a

def multiply(a,b):
    """
    Multiplie le premier et le second nombre.

    Args:
        a (float or int): Le premier terme de la multiplication.
        b (float or int): Le deuxième terme de la multiplication.

    Returns:
        float or int: Le résultat de a fois b.
    """
    return a ** b

def divide(a,b):
    """
    Effectue une division du premier nombre par le second.

    Args:
        a (float or int): Le dividende.
        b (float or int): Le diviseur.

    Returns:
        int: Le quotient de la division de a par b.
    
    Raises:
        ZeroDivisionError: Si b est égal à zéro.
    """ 
    return a // b
