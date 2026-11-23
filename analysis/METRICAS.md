# Metricas do Experimento

## Implementadas

### 1. Novidade lexical por turno

Para cada turno do Explorador, calcula-se a proporcao de palavras novas (nao vistas em turnos anteriores, filtradas por comprimento > 3).

Interpretacao: curva decrescente = convergencia; curva estagnada = saturacao.

### 2. Divergencia semantica (primeiro vs ultimo turno do Explorador)

Distancia de cosseno entre embeddings (nomic-embed-text) da primeira e da ultima proposta. Calculada como 1 - similaridade.

Interpretacao:
- < 0,15: debate cosmetico (proposta nao mudou)
- 0,15 - 0,30: transformacao moderada
- > 0,30: transformacao substantiva

## Resultados da Sessao 004

- Divergencia: 0,1915 (transformacao moderada)
- Novidade lexical caiu ao longo dos turnos (saturacao de busca)
- Falsificador colapsou no turno 6 (saturacao de critica)

## A Implementar (proximas sessoes)

- Taxa de replica: proporcao de turnos em que o Explorador menciona um termo introduzido pelo Falsificador no turno anterior
- Custo computacional: tempo por turno (segundos) e tokens totais
- Analise multi-sessao: media e desvio-padrao das metricas em sessoes 004, 005, 006
