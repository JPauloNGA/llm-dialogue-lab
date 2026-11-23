import json
import sys
from pathlib import Path
import matplotlib.pyplot as plt

def carregar(caminho):
    with open(caminho, 'r', encoding='utf-8') as f:
        return json.load(f)

def gerar(sessao, saida):
    sid = sessao['sessao_id']
    turnos = sessao['turnos']
    autores = sorted(set(t['autor'] for t in turnos))
    cores = {'qwen': '#1f77b4', 'explorador': '#1f77b4', 'hermes': '#d62728', 'falsificador': '#d62728', 'meta': '#2ca02c'}
    markers = {'qwen': 'o', 'explorador': 'o', 'hermes': 's', 'falsificador': 's', 'meta': '^'}

    fig, ax = plt.subplots(figsize=(10, 5))
    for autor in autores:
        pontos = [t for t in turnos if t['autor'] == autor]
        x = [t['turno'] for t in pontos]
        y = [t.get('palavras', len(t['conteudo'].split())) for t in pontos]
        ax.plot(x, y, marker=markers.get(autor, 'o'), label=autor.capitalize(), color=cores.get(autor, '#888888'))
    ax.set_xlabel('Turno')
    ax.set_ylabel('Palavras')
    ax.set_title('Palavras por turno - ' + sid)
    ax.legend()
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(saida / (sid + '_palavras_por_turno.png'), dpi=150)
    plt.close(fig)

    if any('novidade_lexical' in t for t in turnos):
        fig, ax = plt.subplots(figsize=(10, 5))
        for autor in autores:
            pontos = [t for t in turnos if t['autor'] == autor and 'novidade_lexical' in t]
            if not pontos:
                continue
            x = [t['turno'] for t in pontos]
            y = [t['novidade_lexical'] for t in pontos]
            ax.plot(x, y, marker=markers.get(autor, 'o'), label=autor.capitalize(), color=cores.get(autor, '#888888'))
        ax.set_xlabel('Turno')
        ax.set_ylabel('Novidade lexical')
        ax.set_title('Taxa de novidade lexical por turno - ' + sid)
        ax.legend()
        ax.grid(True, alpha=0.3)
        fig.tight_layout()
        fig.savefig(saida / (sid + '_novidade_lexical.png'), dpi=150)
        plt.close(fig)

    fig, ax = plt.subplots(figsize=(6, 5))
    totais = []
    labels = []
    cores_bar = []
    for autor in autores:
        total = sum(t.get('palavras', len(t['conteudo'].split())) for t in turnos if t['autor'] == autor)
        totais.append(total)
        labels.append(autor.capitalize())
        cores_bar.append(cores.get(autor, '#888888'))
    ax.bar(labels, totais, color=cores_bar)
    ax.set_ylabel('Total de palavras')
    ax.set_title('Volume total por papel - ' + sid)
    for i, v in enumerate(totais):
        ax.text(i, v + max(totais)*0.02, str(v), ha='center', fontweight='bold')
    fig.tight_layout()
    fig.savefig(saida / (sid + '_total_palavras.png'), dpi=150)
    plt.close(fig)

    print('Graficos gerados em ' + str(saida))
    if 'divergencia_primeiro_ultimo' in sessao and sessao['divergencia_primeiro_ultimo'] is not None:
        print('Divergencia semantica primeiro-ultimo explorador: ' + str(sessao['divergencia_primeiro_ultimo']))

if __name__ == '__main__':
    repo = Path(__file__).resolve().parents[2]
    nome = sys.argv[1] if len(sys.argv) > 1 else 'sessao_004.json'
    sessao_path = repo / 'conversations' / nome
    saida = repo / 'analysis' / 'charts'
    saida.mkdir(parents=True, exist_ok=True)
    sessao = carregar(sessao_path)
    gerar(sessao, saida)
