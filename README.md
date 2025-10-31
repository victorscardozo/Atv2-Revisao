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

⚙️Requisitos

Python 3.10+

Nenhuma biblioteca externa é necessária.

(Opcional — para saída colorida no terminal)
pip install rich



🚀 Como Executar
1️⃣ Clonar ou baixar o projeto
git clone https://github.com/SEU-USUARIO/Atv2-Revisao.git
cd Atv2-Revisao

2️⃣ Executar a simulação completa

No terminal do VS Code ou PowerShell:

py -3 -m scripts.simular


💡 Dica: Sempre execute a partir da raiz do projeto (onde está a pasta data).



🔁 Fluxo do Sistema
Cliente → Pedido → Cálculo de Rota → Atualização de Status → Conclusão

Etapas simuladas

Receber Pedido
Cria um pedido com cliente e produto.

Processar Rota
Calcula qual galpão está mais próximo usando distância euclidiana.

Atualizar Status
Define o status final (ENVIADO) e exibe os resultados.



🧮 Exemplo de Execução
py -3 -m scripts.simular

Saída esperada
🚚 INICIANDO SIMULAÇÃO LOGÍSTICA...
------------------------------------------------------------
📦 Pedido recebido com sucesso!
   → ID: pd-0101
   → Status: CONFIRMADO

🧭 Rota definida:
   → Galpão: g-001
   → Tipo de Rota: R-ECONOMICA-G-001

📤 Pedido atualizado!
   → ID: pd-0101
   → Novo Status: ENVIADO
------------------------------------------------------------
✅ Fluxo finalizado com sucesso!

📊 ESTADO FINAL DOS DADOS:
╔══════════════════════╗
║ Pedidos              ║
╚══════════════════════╝
{
  "_seq": 101,
  "itens": {
    "pd-0101": {
      "pedido_id": "pd-0101",
      "cliente_id": "c-001",
      "produto_id": "p-001",
      "status": "ENVIADO",
      "galpao_destino": "g-001",
      "rota": "R-ECONOMICA-G-001"
    }
  }
}


🧠 Lógica de Cálculo de Distância

O cálculo da distância é feito utilizando a distância euclidiana, conforme a fórmula abaixo:

𝑑=√((𝑥1−𝑥2)2+(𝑦1−𝑦2)2)d=√((x1−x)2+(y1−y2)2)

O galpão com menor distância ao cliente é selecionado para a entrega.



💾 Funcionamento Interno

O sistema é dividido em três camadas principais:

1. lib/

Contém funções utilitárias, como:

jsondb.py: leitura e escrita de arquivos JSON;

distancia.py: cálculo da distância entre pontos.

2. services/

Responsável pela lógica principal:

orders.py: gerencia pedidos, status e filas;

routing.py: define o galpão mais próximo.

3. scripts/

Contém scripts de execução:

simular.py: coordena todo o fluxo de simulação (entrada → rota → status).




📈 Fluxo Simplificado
📦 Pedido Recebido
       ↓
🧭 Cálculo de Rota (galpão mais próximo)
       ↓
🚚 Atualização de Status → ENVIADO
       ↓
✅ Fim do Processo
