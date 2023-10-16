# Importar bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import accuracy_score

# Carregar o conjunto de dados
data = load_breast_cancer()
x, y = data.data, data.target

# Dividir os dados em conjuntos de treinamento e teste
x_treino, X_teste, y_treino, Y_teste = train_test_split(x, y)
print(f"x_treino: {x_treino.shape}\nX_teste: {X_teste.shape}")

# Converter o conjunto de dados para um DataFrame do Pandas
data_df = pd.DataFrame(data.data, columns=data.feature_names)
data_df['Target'] = data.target

# Exibir uma prévia dos dados
print(data_df.head())

# Criar o modelo de classificação
preditor = DecisionTreeClassifier(max_leaf_nodes=4)

# Treinar o modelo
preditor.fit(x_treino, y_treino)

# Visualizar a árvore de decisão
from sklearn.tree import plot_tree
plt.figure(figsize=(10, 6))
plot_tree(preditor, filled=True)
plt.show()

# Validar o modelo
resultado_pred = preditor.predict(X_teste)
accuracy = accuracy_score(resultado_pred, Y_teste)
print(f"Acurácia do modelo: {accuracy:.2f}")

# Testar o modelo
exemplo = [X_teste[11]]
predicao = preditor.predict(exemplo)
print(f"Exemplo de entrada: {exemplo}")
print(f"Previsão para o exemplo: {predicao}")
print(f"Rótulo verdadeiro para o exemplo: {Y_teste[11]}")
print(f"Correto? {predicao[0] == Y_teste[11]}")
