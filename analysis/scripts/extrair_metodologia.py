import json
from pathlib import Path

repo = Path(__file__).resolve().parents[2]
sessao = json.load(open(repo / 'conversations' / 'sessao_004.json', encoding='utf-8'))
turnos = sessao['turnos']

explorador = [t for t in turnos if t['autor'] == 'explorador']
falsificadores = [t for t in turnos if t['autor'] == 'falsificador']
meta = [t for t in turnos if t['autor'] == 'meta']

primeira = explorador[0]['conteudo']
ultima = explorador[-1]['conteudo']
ultima_critica = falsificadores[-1]['conteudo']
meta_txt = meta[-1]['conteudo'] if meta else '(sem meta-reflexao)'

md = []
md.append('# Metodologia Gerada - Sessao 004')
md.append('')
md.append('## Topico')
md.append('')
md.append(sessao['topico'])
md.append('')
md.append('## Proposta Inicial (Turno 1)')
md.append('')
md.append(primeira)
md.append('')
md.append('## Meta-Reflexao (Turno 3)')
md.append('')
md.append(meta_txt)
md.append('')
md.append('## Ultima Critica do Falsificador (Turno 6)')
md.append('')
md.append(ultima_critica)
md.append('')
md.append('## Proposta Final (Turno 6)')
md.append('')
md.append(ultima)
md.append('')
md.append('## Metricas Objetivas')
md.append('')
md.append('- Divergencia semantica (primeiro vs ultimo explorador): ' + str(sessao['divergencia_primeiro_ultimo']))
md.append('- Total de palavras - Explorador: ' + str(sum(t.get('palavras',0) for t in explorador)))
md.append('- Total de palavras - Falsificador: ' + str(sum(t.get('palavras',0) for t in falsificadores)))

out = repo / 'results' / 'METODOLOGIA_GERADA.md'
out.write_text('\n'.join(md), encoding='utf-8')
print('Salvo em ' + str(out))
