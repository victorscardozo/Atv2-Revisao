# lib/jsondb.py
import json
from pathlib import Path
from typing import Any

# caminho raiz do projeto (pasta acima de /lib)
ROOT = Path(__file__).resolve().parents[1]

def _path(rel: str) -> Path:
    return ROOT / rel

def read_json(rel_path: str) -> Any:
    """Lê um arquivo JSON relativo à raiz do projeto."""
    p = _path(rel_path)
    if not p.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {p}")
    with p.open("r", encoding="utf-8") as f:
        return json.load(f)

def write_json(rel_path: str, data: Any) -> None:
    """Grava um objeto Python como JSON (indentado) no caminho relativo informado."""
    p = _path(rel_path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
