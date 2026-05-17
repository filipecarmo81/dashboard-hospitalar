from flask import Flask, render_template, jsonify
from datetime import datetime
import random

app = Flask(__name__)


def gerar_indicadores():
    """Gera indicadores hospitalares fictícios para o dashboard."""
    unidades = ["Hospital Central", "Unidade Norte", "Unidade Sul", "Pronto-Socorro"]
    return {
        "ocupacao": [
            {"unidade": u, "taxa": random.randint(55, 95)} for u in unidades
        ],
        "custo_medio_paciente": random.randint(1800, 3200),
        "pacientes_internados": random.randint(180, 320),
        "tempo_medio_espera_min": random.randint(15, 90),
        "cirurgias_hoje": random.randint(20, 60),
        "alertas": [
            {"tipo": "critico", "mensagem": "UTI Norte com 92% de ocupação"},
            {"tipo": "atencao", "mensagem": "Estoque de antibiótico X abaixo do mínimo"},
            {"tipo": "info", "mensagem": "12 altas previstas para as próximas 4h"},
        ],
        "atualizado_em": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
    }


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/indicadores")
def api_indicadores():
    return jsonify(gerar_indicadores())


@app.route("/health")
def health():
    return {"status": "ok"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
