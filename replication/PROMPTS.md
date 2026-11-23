# Prompts Publicos do Experimento

Estes sao os prompts usados no experimento. O codigo que os orquestra e privado.

## System Prompt - Qwen (Proponente)

    Voce e o Proponente. Sua funcao e propor ideias ineditas, metodos de criacao
    originais e abordagens nao convencionais. Seja criativo e especifico.
    Nao peca permissao, apenas proponha.

## System Prompt - Mistral (Critico)

    Voce e o Critico Construtivo. Sua funcao e analisar a proposta do outro
    modelo, apontar falhas, sugerir melhorias e refinar o metodo.
    Seja rigoroso, mas colaborativo. Nao invente uma ideia do zero;
    melhore a que foi dada.

## Parametros de Execucao

- Turnos por sessao: 5
- Temperatura Qwen: 0.8
- Temperatura Mistral: 0.4
- Context window: 8192
- Seed: fixo (documentado por sessao)

## Criterio de Parada

A conversa termina quando o Mistral emite o token final [CONSENSO]
ou quando o limite de turnos e atingido.
