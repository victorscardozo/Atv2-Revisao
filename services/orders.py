# services/orders.py
from typing import Dict
from lib.jsondb import read_json, write_json
from services.routing import escolher_galpao_simples, desempate_pelo_caminho_total

# caminhos relativos para os "bancos"
CLIENTES = "data/clientes.json"
GALPOES  = "data/galpoes.json"
PRODUTOS = "data/produtos.json"
PEDIDOS  = "data/pedidos.json"
FILAS    = "data/filas.json"

def _next_pedido_id(pedidos_db: Dict) -> str:
    seq = int(pedidos_db.get("_seq", 100)) + 1
    pedidos_db["_seq"] = seq
    return f"pd-{seq:04d}"

def receber_pedido(cliente_id: str, produto_id: str) -> Dict:
    clientes = read_json(CLIENTES)
    produtos = read_json(PRODUTOS)
    pedidos  = read_json(PEDIDOS)
    filas    = read_json(FILAS)

    if cliente_id not in clientes:
        raise ValueError("Cliente inexistente")
    if produto_id not in produtos:
        raise ValueError("Produto inexistente")

    pedido_id = _next_pedido_id(pedidos)
    pedidos["itens"][pedido_id] = {
        "pedido_id": pedido_id,
        "cliente_id": cliente_id,
        "produto_id": produto_id,
        "status": "CONFIRMADO",
        "galpao_destino": None,
        "rota": None
    }

    filas["recebidos"].append(pedido_id)
    filas["prontos_para_rota"].append(pedido_id)

    write_json(PEDIDOS, pedidos)
    write_json(FILAS, filas)

    return {"ok": True, "pedido_id": pedido_id, "status": "CONFIRMADO"}

def processar_rota() -> Dict:
    """
    Pega um pedido da fila 'prontos_para_rota', escolhe o galpão e grava rota.
    """
    clientes = read_json(CLIENTES)
    galpoes  = read_json(GALPOES)
    produtos = read_json(PRODUTOS)
    pedidos  = read_json(PEDIDOS)
    filas    = read_json(FILAS)

    if not filas["prontos_para_rota"]:
        return {"ok": False, "msg": "Nenhum pedido na fila"}

    pedido_id = filas["prontos_para_rota"].pop(0)
    p = pedidos["itens"][pedido_id]

    geo_cli = tuple(clientes[p["cliente_id"]]["geo"])
    geo_prod = tuple(produtos[p["produto_id"]]["geo"])

    # Regra principal: galpão mais próximo do cliente
    g_simple, _ = escolher_galpao_simples(geo_cli, galpoes)

    # (opcional) melhor pelo caminho total Produto->Galpão->Cliente
    g_total, _ = desempate_pelo_caminho_total(geo_prod, geo_cli, galpoes)

    galpao_escolhido = g_simple if g_simple == g_total else g_simple

    p["galpao_destino"] = galpao_escolhido
    p["rota"] = f"R-ECONOMICA-{galpao_escolhido.upper()}"
    p["status"] = "EM_ROTA"

    filas["roteados"].append(pedido_id)

    write_json(PEDIDOS, pedidos)
    write_json(FILAS, filas)

    return {"ok": True, "pedido_id": pedido_id, "galpao": galpao_escolhido, "rota": p["rota"]}

def atualizar_status(pedido_id: str, novo_status: str) -> Dict:
    pedidos = read_json(PEDIDOS)
    if pedido_id not in pedidos["itens"]:
        return {"ok": False, "msg": "Pedido inexistente"}

    pedidos["itens"][pedido_id]["status"] = novo_status
    write_json(PEDIDOS, pedidos)
    return {"ok": True, "pedido_id": pedido_id, "status": novo_status}
