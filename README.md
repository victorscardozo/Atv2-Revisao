# 🚚 **Atv2 - Revisão: Simulação de Logística com Python**

Um sistema simples e didático desenvolvido em **Python puro**, com o objetivo de simular um **fluxo logístico**: recebimento de pedidos, cálculo do galpão mais próximo e atualização de status de entrega.  

O "banco de dados" é armazenado em arquivos **JSON**, e o sistema foi projetado para ser **Simples, organizado e de fácil entendimento**.

---

## 🧭 **Objetivo do Projeto**

Dado um **produto**, um **cliente** e os **centros logísticos disponíveis**, o sistema identifica **qual galpão está mais próximo do cliente** e processa o pedido da forma mais eficiente possível.

O projeto foi estruturado para fins **didáticos** (atividade acadêmica), simulando uma arquitetura escalável semelhante à utilizada em sistemas de logística reais.

---

## 🧩 **Estrutura do Projeto**

```plaintext
Atv2-Revisao/
├─ data/                ← Base de dados em JSON (simulação de banco)
│  ├─ clientes.json
│  ├─ galpoes.json
│  ├─ produtos.json
│  ├─ pedidos.json
│  └─ filas.json
│
├─ lib/                 ← Funções utilitárias (cálculo e manipulação de JSON)
│  ├─ distancia.py
│  └─ jsondb.py
│
├─ services/            ← Camada de regras de negócio
│  ├─ orders.py         ← Gerencia pedidos, filas e status
│  └─ routing.py        ← Calcula o galpão mais próximo
│
├─ scripts/             ← Scripts executáveis do sistema
│  └─ simular.py        ← Simula todo o fluxo logístico
│
└─ README.md            ← Este arquivo
