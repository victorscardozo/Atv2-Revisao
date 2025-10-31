# services/routing.py
from typing import Dict, Tuple
from lib.distancia import distancia_euclidiana

Geo = Tuple[float, float]

def escolher_galpao_simples(geo_cliente: Geo, galpoes: Dict[str, Dict]) -> Tuple[str, float]:
    melhor_id = None
    melhor_dist = float("inf")
    for gid, g in galpoes.items():
        d = distancia_euclidiana(tuple(g["geo"]), geo_cliente)
        if d < melhor_dist:
            melhor_id, melhor_dist = gid, d
    return melhor_id, melhor_dist

def desempate_pelo_caminho_total(geo_produto: Geo, geo_cliente: Geo, galpoes: Dict[str, Dict]) -> Tuple[str, float]:
    melhor_id = None
    melhor_total = float("inf")
    for gid, g in galpoes.items():
        geo_g = tuple(g["geo"])
        total = distancia_euclidiana(geo_produto, geo_g) + distancia_euclidiana(geo_g, geo_cliente)
        if total < melhor_total:
            melhor_id, melhor_total = gid, total
    return melhor_id, melhor_total
