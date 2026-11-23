# LLM Dialogue Lab

Abstracao experimental para interacao autonoma entre LLMs de diferentes provedores, com o objetivo de sintetizar metodos de criacao ineditos, sem replicar conteudo da internet.

## Motivacao

Modelos de linguagem de diferentes arquiteturas (Qwen vs. Mistral) possuem "vieses cognitivos" distintos. Ao coloca-los em dialogo estruturado (Proponente vs. Critico), emergem sinteses que nenhum dos dois geraria isoladamente.

## Stack

- **Runtime local**: Ollama
- **Modelo A (Proponente)**: Qwen 2.5 7B
- **Modelo B (Critico)**: Mistral 7B
- **Orquestracao**: Script privado (nao publicado neste repo)
- **Analise**: Python + Matplotlib (outputs publicados em `analysis/`)

## Estrutura do Repositorio

| Pasta | Conteudo |
|-------|----------|
| `conversations/` | Historico bruto dos dialogos (JSON) |
| `results/` | Metodologias e sinteses finais geradas |
| `analysis/` | Graficos, metricas e visualizacoes |
| `replication/` | Instrucoes para replicar o experimento |

## Principais Resultados

> _Em construcao. Os resultados serao publicados apos a primeira rodada de dialogos._

## Como Replicar

Veja [replication/SETUP.md](replication/SETUP.md). Voce nao precisa do nosso codigo-fonte: os prompts e parametros estao documentados em [replication/PROMPTS.md](replication/PROMPTS.md).

## Autor

Joao Paulo - [GitHub](https://github.com/JPauloNGA)
