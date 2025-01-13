import requests
import json
import argparse

# Função para enviar a solicitação POST
def get_recommendations(songs, server_url):
    payload = {"songs": songs}

    try:
        # Enviar solicitação POST
        response = requests.post(server_url, json=payload)

        # Verificar o status da resposta
        if response.status_code == 200:
            recommendations = response.json()
            print("Recomendações:")
            print(json.dumps(recommendations, indent=4))
        else:
            print(f"Erro: {response.status_code}")
            print(response.text)

    except requests.exceptions.RequestException as e:
        print(f"Erro ao se conectar ao servidor: {e}")

def main():
    # Argumentos do cliente
    parser = argparse.ArgumentParser(description="Cliente REST API para recomendar músicas.")
    parser.add_argument("--songs", nargs="+", required=True, help="Lista de músicas para recomendação.")
    parser.add_argument("--url", default="http://localhost:52021/api/recommend", help="URL do servidor REST API.")
    args = parser.parse_args()

    get_recommendations(args.songs, args.url)

if __name__ == "__main__":
    main()
