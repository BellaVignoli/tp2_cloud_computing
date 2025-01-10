from fpgrowth_py import fpgrowth
import pickle

# Carregar os dados do CSV (exemplo)
import pandas as pd

# Carregar o dataset

dataset_path = os.getenv('DATASET_PATH', '/app/datasets')  # Valor padrão: '/app/datasets'
dataset_name = os.getenv("DATASET_NAME", "2023_spotify_ds2.csv")
# file_path = "/app/datasets/2023_spotify_ds1.csv"

file_path = Path(dataset_base_path) / dataset_name

df = pd.read_csv(file_path)

# Pré-processamento dos dados (transformar playlists em listas de itens)
itemSetList = df.groupby('pid')['track_name'].apply(list).tolist()

# Gerar regras usando o algoritmo FP-Growth
min_support = 0.1  # 10% de suporte mínimo
min_confidence = 0.5  # 50% de confiança mínima

freqItemSet, rules = fpgrowth(itemSetList, minSupRatio=min_support, minConf=min_confidence)

# Salvar o modelo em um arquivo pickle
model_path = "/arq/recommendation_model.pickle"
with open(model_path, 'wb') as f:
    pickle.dump(rules, f)

print("Modelo gerado e salvo com sucesso!")