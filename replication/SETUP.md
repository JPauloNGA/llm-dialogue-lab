# Setup para Replicacao

## Pre-requisitos

- Ollama instalado (https://ollama.com)
- Python 3.10+
- Aproximadamente 12 GB de espaco livre em disco

## Passo 1: Baixar os modelos

Abra o terminal e execute:

    ollama pull qwen2.5:7b
    ollama pull mistral:7b

## Passo 2: Verificar que estao funcionando

    ollama run qwen2.5:7b Responda apenas: OK
    ollama run mistral:7b Responda apenas: OK

## Passo 3: Implementar o orquestrador

O codigo-fonte do orquestrador NAO e publicado neste repositorio
por opcao do autor. Porem, os prompts, parametros e a logica completa
estao descritos em:

- PROMPTS.md - prompts de sistema e de turno
- SCRIPTS_EXAMPLE.md - pseudocodigo e estrutura

Qualquer pessoa com conhecimento basico de Python e a biblioteca
ollama consegue reproduzir o experimento em menos de 30 minutos.

## Passo 4: Comparar resultados

Apos rodar o experimento, compare suas conversas com as publicadas
em ../conversations/. As metricas esperadas estao em ../analysis/METRICAS.md.
