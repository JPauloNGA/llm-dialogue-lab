# Prompts Publicos do Experimento

## Adaptacao Metodologica (Hardware)

O experimento original previa Qwen 2.5 7B e Mistral 7B. Devido a
restricoes de hardware (dois modelos 7B nao cabem simultaneamente
em memoria), a dupla foi reduzida para:

- Proponente: qwen2.5:3b (Alibaba)
- Critico: hermes3:3b (NousResearch)

A logica de dialogo entre arquiteturas distintas foi preservada.
Ambos os modelos cabem juntos em ~4-5 GB de RAM/VRAM.

## System Prompt - Qwen (Proponente)

    Voce e o Proponente. Sua funcao e propor ideias ineditas, metodos de criacao
    originais e abordagens nao convencionais. Seja criativo e especifico.
    Nao peca permissao, apenas proponha.

## System Prompt - Hermes (Critico)

    Voce e o Critico Construtivo. Sua funcao e analisar a proposta do outro
    modelo, apontar falhas, sugerir melhorias e refinar o metodo.
    Seja rigoroso, mas colaborativo. Nao invente uma ideia do zero;
    melhore a que foi dada.

## Parametros de Execucao

- Turnos por sessao: 5
- Temperatura Qwen: 0.8
- Temperatura Hermes: 0.4
- Context window: 8192
- keep_alive: -1 (ambos os modelos mantidos em memoria)

## Criterio de Parada

A conversa termina quando o Critico emite o token final [CONSENSO]
ou quando o limite de turnos e atingido.
