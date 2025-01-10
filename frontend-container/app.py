from flask import Flask, request, jsonify
import pickle
import os

# Inicializar o servidor Flask
app = Flask(__name__)
app.model = pickle.load(open("/arq/recommendation_model.pickle", "rb"))

# Carregar o modelo salvo
with open("/arq/recommendation_model.pickle", 'rb') as f:
    rules = pickle.load(f)

@app.route("/api/recommend", methods=["POST"])
def recommend():
    # Obter a lista de músicas do corpo da solicitação
    data = request.get_json()
    liked_songs = set(data.get("songs", []))

    # Gerar recomendações com base nas regras
    recommendations = []
    for rule in rules:
        antecedent, consequent, confidence = rule
        if liked_songs.issuperset(antecedent) and consequent not in liked_songs:
            print(f"Regra aplicável encontrada: {rule}")
            recommendations.extend(consequent)
        
    # Remover duplicados
    recommendations = list(set(recommendations))[:10]
    # print(f"Recommendations: {recommendations}")

    # Retornar resposta JSON
    return jsonify({
        "songs": recommendations,
        "version": "1.0",
        "model_date": "2025-01-09"
    })

# Executar o servidor na porta 52032
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=52032, debug=True)