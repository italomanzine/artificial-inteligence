# Função para exibir o tabuleiro
def exibir_tabuleiro(tabuleiro):
    print("   0   1   2")
    for i, row in enumerate(tabuleiro):
        print(i, end='  ')
        for j, cell in enumerate(row):
            print(cell, end='')
            if j < 2:
                print(" | ", end='')
        print()
        if i < 2:
            print("  ---|---|---")

# Função para verificar o status do jogo
def verificar_status(tabuleiro):
    # Verifica se algum jogador venceu nas linhas
    for row in tabuleiro:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0]

    # Verifica se algum jogador venceu nas colunas
    for col in range(3):
        if tabuleiro[0][col] == tabuleiro[1][col] == tabuleiro[2][col] and tabuleiro[0][col] != ' ':
            return tabuleiro[0][col]

    # Verifica se algum jogador venceu nas diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] and tabuleiro[0][0] != ' ':
        return tabuleiro[0][0]
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] and tabuleiro[0][2] != ' ':
        return tabuleiro[0][2]

    # Verifica se o jogo terminou em empate
    if all(row.count('X') + row.count('O') == 3 for row in tabuleiro):
        return 'Empate'

    # O jogo continua
    return None

# Função para a jogada do jogador
def jogada_jogador(tabuleiro):
    while True:
        try:
            linha = int(input("Escolha a linha (0, 1 ou 2): "))
            coluna = int(input("Escolha a coluna (0, 1 ou 2): "))
            if 0 <= linha <= 2 and 0 <= coluna <= 2 and tabuleiro[linha][coluna] == ' ':
                tabuleiro[linha][coluna] = 'X'
                break
            else:
                print("Jogada inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite números inteiros.")

# Função para a jogada do computador (usando Minimax com Alpha-Beta)
def jogada_computador(tabuleiro):
    def minimax(tabuleiro, profundidade, jogador, alpha, beta):

        # Verifica o estado atual do tabuleiro
        status = verificar_status(tabuleiro)

        # Atribui valores para representar os estados do jogo
        if status == 'X':
            return -1
        elif status == 'O':
            return 1
        elif status == 'Empate':
            return 0

        if jogador == 'O':
            melhor_valor = float('-inf') # Valor mínimo para 'O'
            for i in range(3):
                for j in range(3):
                    if tabuleiro[i][j] == ' ':
                        tabuleiro[i][j] = jogador
                        valor = minimax(tabuleiro, profundidade + 1, 'X', alpha, beta)
                        tabuleiro[i][j] = ' '
                        melhor_valor = max(melhor_valor, valor)
                        alpha = max(alpha, valor)

                        # Poda alfa-beta
                        if beta <= alpha:
                            break
            return melhor_valor
        else:
            melhor_valor = float('inf') # Valor máximo para 'X'
            for i in range(3):
                for j in range(3):
                    if tabuleiro[i][j] == ' ':
                        tabuleiro[i][j] = jogador
                        valor = minimax(tabuleiro, profundidade + 1, 'O', alpha, beta)
                        tabuleiro[i][j] = ' '
                        melhor_valor = min(melhor_valor, valor)
                        beta = min(beta, valor)

                        # Poda alfa-beta
                        if beta <= alpha:
                            break
            return melhor_valor

    melhor_valor = float('-inf') # Valor mínimo para 'O'
    melhor_jogada = None

    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == ' ':
                tabuleiro[i][j] = 'O'
                valor = minimax(tabuleiro, 0, 'X', float('-inf'), float('inf'))
                tabuleiro[i][j] = ' '

                # Encontra a melhor jogada para 'O'
                if valor > melhor_valor:
                    melhor_valor = valor
                    melhor_jogada = (i, j)

    if melhor_jogada:
        tabuleiro[melhor_jogada[0]][melhor_jogada[1]] = 'O'

# Função principal do jogo
def jogar_jogo_da_velha():
    tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
    jogador_atual = 'X'

    print("Bem-vindo ao Jogo da Velha!")

    while True:
        exibir_tabuleiro(tabuleiro)
        print(f"É a vez do jogador {jogador_atual}")
        if jogador_atual == 'X':
            jogada_jogador(tabuleiro)
        else:
            jogada_computador(tabuleiro)
        status = verificar_status(tabuleiro)

        if status == 'X':
            exibir_tabuleiro(tabuleiro)
            print("O jogador X venceu!")
            break
        elif status == 'O':
            exibir_tabuleiro(tabuleiro)
            print("O jogador O venceu!")
            break
        elif status == 'Empate':
            exibir_tabuleiro(tabuleiro)
            print("O jogo terminou em empate!")
            break

        jogador_atual = 'X' if jogador_atual == 'O' else 'O'

if __name__ == "__main__":
    jogar_jogo_da_velha()
