# lib/distancia.py
from typing import Tuple
Ponto = Tuple[float, float]

def distancia_euclidiana(a: Ponto, b: Ponto) -> float:
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2) ** 0.5
