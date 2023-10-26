# Importar bibliotecas
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

# Carregar o conjunto de dados
data = pd.read_csv('weather.csv')

# Pré-processamento: lidar com valores faltantes, converter colunas categóricas, etc.
# Exemplo de preenchimento de valores faltantes com a média da coluna
data = data.fillna(data.mean())

# Converter colunas categóricas em valores numéricos
le = LabelEncoder()
for col in data.select_dtypes(include='object').columns:
    data[col] = le.fit_transform(data[col])

# Separar as variáveis independentes e a variável dependente
X = data.drop('RainTomorrow', axis=1)
y = data['RainTomorrow']

# Dividir os dados em conjuntos de treinamento e teste
X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.2, random_state=0)

# Criar o preditor do tipo KNN
pred = KNeighborsClassifier(n_neighbors=5)

# Treinar o preditor
pred.fit(X_treino, y_treino)

# Analisar a eficácia do preditor
y_pred = pred.predict(X_teste)
accuracy = accuracy_score(y_teste, y_pred)
print(f'Acurácia: {accuracy * 100:.2f}%')
