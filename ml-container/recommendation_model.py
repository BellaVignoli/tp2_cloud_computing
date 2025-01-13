from fpgrowth_py import fpgrowth
import pickle

# Carregar os dados do CSV
import pandas as pd

# Carregar o dataset
file_path = "/app/datasets/2023_spotify_ds1.csv"
df = pd.read_csv(file_path)

# Pré-processamento dos dados
itemSetList = df.groupby('pid')['track_name'].apply(list).tolist()

# Gerar regras usando o algoritmo FP-Growth
min_support = 0.1  # 10% de suporte mínimo
min_confidence = 0.5  # 50% de confiança mínima

freqItemSet, rules = fpgrowth(itemSetList, minSupRatio=min_support, minConf=min_confidence)

# Salvar o modelo em um arquivo pickle
model_path = "/arq/recommendation_model.pickle"
with open(model_path, 'wb') as f:
    pickle.dump(rules, f)
