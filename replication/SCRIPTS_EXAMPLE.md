# Pseudocodigo do Orquestrador

Este arquivo descreve a logica do orquestrador sem entregar o codigo-fonte.

## Fluxo

1. Definir topico inicial do debate
2. Carregar system prompts de Qwen (Proponente) e Mistral (Critico)
3. Loop de N turnos:
   a. Qwen recebe historico e propoe
   b. Mistral recebe historico + proposta de Qwen e critica
   c. Salvar turno no JSON de sessao
4. Detectar criterio de parada ([CONSENSO] ou limite de turnos)
5. Exportar sessao final para conversations/

## Biblioteca usada

    import ollama
    response = ollama.chat(model=..., messages=[...])

## Formato de saida

O JSON de sessao segue o schema descrito em conversations/EXEMPLO_CONVERSA.json.
