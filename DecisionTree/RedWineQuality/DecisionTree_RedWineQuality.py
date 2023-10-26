# Importar bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Carregar o conjunto de dados
data = pd.read_csv('winequality-red.csv')

# Verifique se você precisa separar os dados em features (x) e target (y)
# Supondo que a última coluna é o target e as demais são as features
x = data.iloc[:, :-1].values
y = data.iloc[:, -1].values

# Dividir os dados em conjuntos de treinamento e teste
x_treino, X_teste, y_treino, Y_teste = train_test_split(x, y)
print(f"x_treino: {x_treino.shape}\nX_teste: {X_teste.shape}")

# Converter o conjunto de dados para um DataFrame do Pandas
data_df = pd.DataFrame(x, columns=data.columns[:-1])
data_df['quality'] = y

# Exibir uma prévia dos dados
print(data_df.head())

# Criar o modelo de classificação
preditor = DecisionTreeClassifier(max_leaf_nodes=5)

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
