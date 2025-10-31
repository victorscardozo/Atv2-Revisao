
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))


import argparse
from pathlib import Path
from lib.jsondb import read_json, write_json
from services.orders import receber_pedido, processar_rota, atualizar_status

ROOT = Path(__file__).resolve().parents[1]

def reset():
    write_json("data/pedidos.json", {"_seq": 100, "itens": {}})
    write_json("data/filas.json", {"recebidos": [], "prontos_para_rota": [], "roteados": []})
    print("OK: reset feito.")

def exemplo_fluxo():
    print("\n🚚 INICIANDO SIMULAÇÃO LOGÍSTICA...\n" + "-"*60)

    # 1️⃣ Receber pedido
    r1 = receber_pedido(cliente_id="c-001", produto_id="p-001")
    print(f"📦 Pedido recebido com sucesso!\n   → ID: {r1['pedido_id']}\n   → Status: {r1['status']}\n")

    # 2️⃣ Processar rota
    r2 = processar_rota()
    print(f"🧭 Rota definida:\n   → Galpão: {r2['galpao']}\n   → Tipo de Rota: {r2['rota']}\n")

    # 3️⃣ Atualizar status
    pid = r1["pedido_id"]
    r3 = atualizar_status(pid, "ENVIADO")
    print(f"📤 Pedido atualizado!\n   → ID: {r3['pedido_id']}\n   → Novo Status: {r3['status']}\n")

    print("-"*60 + "\n✅ Fluxo finalizado com sucesso!\n")

    # 4️⃣ Exibir bancos (resumo)
    print("📊 ESTADO FINAL DOS DADOS:\n")
    print("╔══════════════════════╗")
    print("║ Clientes             ║")
    print("╚══════════════════════╝")
    print(read_json("data/clientes.json"))
    print("\n╔══════════════════════╗")
    print("║ Galpões              ║")
    print("╚══════════════════════╝")
    print(read_json("data/galpoes.json"))
    print("\n╔══════════════════════╗")
    print("║ Produtos             ║")
    print("╚══════════════════════╝")
    print(read_json("data/produtos.json"))
    print("\n╔══════════════════════╗")
    print("║ Pedidos              ║")
    print("╚══════════════════════╝")
    print(read_json("data/pedidos.json"))
    print("\n╔══════════════════════╗")
    print("║ Filas                ║")
    print("╚══════════════════════╝")
    print(read_json("data/filas.json"))

def mostrar_bancos():
    for rel in ["data/clientes.json", "data/galpoes.json", "data/produtos.json", "data/pedidos.json", "data/filas.json"]:
        print(f"\n== {rel} ==")
        print(read_json(rel))

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Simulador logístico simples")
    ap.add_argument("acao", nargs="?", default="run",
                    choices=["run", "reset", "mostrar", "receber", "rota", "status"],
                    help="run=fluxo completo | reset | mostrar | receber | rota | status")
    ap.add_argument("--pedido", help="id do pedido para 'status'")
    ap.add_argument("--novo-status", default="ENVIADO", help="novo status para 'status'")

    args = ap.parse_args()

    if args.acao == "reset":
        reset()
    elif args.acao == "mostrar":
        mostrar_bancos()
    elif args.acao == "receber":
        print(receber_pedido("c-001", "p-001"))
    elif args.acao == "rota":
        print(processar_rota())
    elif args.acao == "status":
        if not args.pedido:
            print("Use --pedido <id>")
        else:
            print(atualizar_status(args.pedido, args.novo_status))
    else:
        # fluxo completo
        reset()
        exemplo_fluxo()
        print("\n--- Bancos após o fluxo ---")
        mostrar_bancos()
