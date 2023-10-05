# Tabela de distâncias das cidades até Três Corações (Valores H)
distancias = {
    'Paraguaçu': 69,
    'Machado': 100,
    'Alfenas': 98,
    'Elói Mendes': 49,
    'Três Corações': 0,
    'Varginha': 33,
    'Monsenhor Paulo': 44,
    'Campos Gerais': 114,
    'Santana da Vargem': 77,
    'Três Pontas': 62,
    'Nepomuceno': 79,
    'Ribeirão Vermelho': 90,
    'Carmo da Cachoeira': 39
}

# Tabela de distâncias entre cidades (Valores G)
distancias_entre_cidades = {
    ('Paraguaçu', 'Machado'): 32,
    ('Paraguaçu', 'Alfenas'): 30,
    ('Paraguaçu', 'Elói Mendes'): 23,
    ('Machado', 'Monsenhor Paulo'): 60,
    ('Monsenhor Paulo', 'Três Corações'): 44,
    ('Elói Mendes', 'Varginha'): 18,
    ('Varginha', 'Três Corações'): 33,
    ('Alfenas', 'Campos Gerais'): 35,
    ('Campos Gerais', 'Santana da Vargem'): 35,
    ('Santana da Vargem', 'Três Pontas'): 18,
    ('Três Pontas', 'Varginha'): 29,
    ('Santana da Vargem', 'Nepomuceno'): 31,
    ('Nepomuceno', 'Ribeirão Vermelho'): 39,
    ('Ribeirão Vermelho', 'Carmo da Cachoeira'): 58,
    ('Carmo da Cachoeira', 'Três Corações'): 39
}

# Função de Busca Gulosa para encontrar o caminho mais curto entre duas cidades
def greedy_search(start_city, target_city):
    current_city = start_city
    path = [current_city]  # Inicializa o caminho com a cidade de início
    total_distance = 0  # Inicializa a distância total como zero

    while current_city != target_city:  # Enquanto não chegarmos à cidade-alvo
        min_distance = float('inf')  # Valor inicial alto para encontrar o mínimo
        next_city = None

        for city in distancias:
            if city != current_city and distancias_entre_cidades.get((current_city, city)):
                distance_to_target = distancias[city]  # Valor H (heurística)
                if distance_to_target < min_distance:
                    min_distance = distance_to_target  # Atualiza a menor distância encontrada
                    next_city = city  # Atualiza a próxima cidade a ser visitada

        if next_city is None:
            break  # Se não houver próxima cidade, encerra a busca

        # Calcula a distância entre a cidade atual e a próxima cidade (Valor G)
        total_distance += distancias_entre_cidades[(current_city, next_city)]
        
        path.append(next_city)  # Adiciona a próxima cidade ao caminho
        current_city = next_city  # Atualiza a cidade atual para a próxima cidade

    return path, total_distance  # Retorna o caminho encontrado e a distância total percorrida

# Cidades de início e destino
start_city = 'Paraguaçu'
target_city = 'Três Corações'

# Chamando a função de Busca Gulosa para encontrar o caminho mais curto
path, total_distance = greedy_search(start_city, target_city)

# Exibindo o resultado
print(f'Caminho mais curto de {start_city} até {target_city}:')
print(' -> '.join(path))
print(f'Distância total percorrida: {total_distance} km')
