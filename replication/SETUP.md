# Setup para Replicacao

## Pre-requisitos

- Ollama instalado (https://ollama.com)
- Python 3.10+
- Aproximadamente 6 GB de espaco livre em disco

## Passo 1: Baixar os modelos

    ollama pull qwen2.5:3b
    ollama pull hermes3:3b

## Passo 2: Verificar que estao funcionando

    ollama run qwen2.5:3b Responda apenas: OK
    ollama run hermes3:3b Responda apenas: OK

## Passo 3: Implementar o orquestrador

O codigo-fonte do orquestrador NAO e publicado neste repositorio.
Os prompts e a logica completa estao em PROMPTS.md e SCRIPTS_EXAMPLE.md.

Dica critica para hardware fraco: use keep_alive=-1 nas chamadas
ollama.chat() para manter ambos os modelos carregados simultaneamente.

## Passo 4: Comparar resultados

Compare suas conversas com as publicadas em ../conversations/.
