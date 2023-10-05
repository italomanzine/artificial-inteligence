# Tabela de distâncias das cidades até Três Corações (Valores H)
distancias_h = {
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
distancias_g = {
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

# Função A* para encontrar o caminho mais curto entre duas cidades
def a_star_search(start_city, target_city):
    open_list = [(distancias_h[start_city], start_city)]  # Lista de nós para explorar
    came_from = {}  # Dicionário para armazenar o caminho
    g_score = {city: float('inf') for city in distancias_h}  # Custos G iniciais
    g_score[start_city] = 0

    while open_list:
        current_g, current_city = open_list.pop(0) # Remove o nó com menor custo f

        if current_city == target_city:
            path = [current_city]
            while current_city in came_from:
                current_city = came_from[current_city]
                path.append(current_city)
            path.reverse()
            return path, g_score[target_city]

        for neighbor in distancias_g:
            if neighbor[0] == current_city:
                tentative_g = g_score[current_city] + distancias_g[neighbor]

                if tentative_g < g_score[neighbor[1]]:
                    came_from[neighbor[1]] = current_city
                    g_score[neighbor[1]] = tentative_g
                    f_score = tentative_g + distancias_h[neighbor[1]]
                    open_list.append((f_score, neighbor[1]))
                    open_list.sort()  # Ordena a lista de acordo com o valor f_score

    return None, float('inf')  # Caminho não encontrado

# Definindo as cidades de início e destino
start_city = 'Paraguaçu'
target_city = 'Três Corações'

# Chamando a função A* para encontrar o caminho mais curto
path, total_distance = a_star_search(start_city, target_city)

# Exibindo o resultado
if path:
    print(f'Caminho mais curto de {start_city} até {target_city}:')
    print(' -> '.join(path))
    print(f'Distância total percorrida: {total_distance} km')
else:
    print(f'Não foi possível encontrar um caminho de {start_city} até {target_city}.')
