import json
from pathlib import Path
import matplotlib.pyplot as plt

def carregar_sessao(caminho):
    with open(caminho, 'r', encoding='utf-8') as f:
        return json.load(f)

def gerar_graficos(sessao, pasta_saida):
    turnos = sessao['turnos']
    qwen = [t for t in turnos if t['autor'] == 'qwen']
    hermes = [t for t in turnos if t['autor'] == 'hermes']

    fig, ax = plt.subplots(figsize=(10, 5))
    x_q = [t['turno'] for t in qwen]
    y_q = [t.get('palavras', len(t['conteudo'].split())) for t in qwen]
    x_h = [t['turno'] for t in hermes]
    y_h = [t.get('palavras', len(t['conteudo'].split())) for t in hermes]
    ax.plot(x_q, y_q, marker='o', label='Qwen (Proponente)', color='#1f77b4')
    ax.plot(x_h, y_h, marker='s', label='Hermes (Critico)', color='#d62728')
    ax.set_xlabel('Turno')
    ax.set_ylabel('Palavras')
    ax.set_title('Tamanho das respostas por turno - ' + sessao['sessao_id'])
    ax.legend()
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    nome1 = sessao['sessao_id'] + '_palavras_por_turno.png'
    fig.savefig(pasta_saida / nome1, dpi=150)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(6, 5))
    total_q = sum(y_q)
    total_h = sum(y_h)
    ax.bar(['Qwen', 'Hermes'], [total_q, total_h], color=['#1f77b4', '#d62728'])
    ax.set_ylabel('Total de palavras')
    ax.set_title('Volume total de contribuicao - ' + sessao['sessao_id'])
    for i, v in enumerate([total_q, total_h]):
        ax.text(i, v + 5, str(v), ha='center', fontweight='bold')
    fig.tight_layout()
    nome2 = sessao['sessao_id'] + '_total_palavras.png'
    fig.savefig(pasta_saida / nome2, dpi=150)
    plt.close(fig)

    print('Graficos gerados em ' + str(pasta_saida))

if __name__ == '__main__':
    repo = Path(__file__).resolve().parents[2]
    sessao_path = repo / 'conversations' / 'sessao_003.json'
    saida = repo / 'analysis' / 'charts'
    saida.mkdir(parents=True, exist_ok=True)
    sessao = carregar_sessao(sessao_path)
    gerar_graficos(sessao, saida)
