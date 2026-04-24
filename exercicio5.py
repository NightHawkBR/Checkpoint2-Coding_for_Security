print("---| CONTADOR DE FREQUÊNCIA DE PALAVRAS |---")

# Recebe o texto digitado pelo usuário e converte para minúsculo
texto = input("\nDigite o texto: ").lower()

# Divide o texto em uma lista de palavras usando os espaços como separador
palavras = texto.split()

# Verifica se o texto não está vazio
if not palavras:
    print("\nNenhuma palavra encontrada no texto.")
else:

    # ── Contagem das palavras ───────────────────────────────

    # Dicionário que armazenará {palavra: contagem}
    frequencia = {}

    # Percorre cada palavra da lista
    for item in palavras:
        # Se a palavra já existe no dicionário, incrementa o contador
        # Se não existe, o .get() retorna 0 e soma 1 (primeiro registro)
        frequencia[item] = frequencia.get(item, 0) + 1

    # Converte o dicionário em uma lista de tuplas [(palavra, contagem), ...]
    lista_frequencia = list(frequencia.items())

    # Ordena a lista usando bubble sort manual:
    for i in range(len(lista_frequencia)):
        for j in range(i + 1, len(lista_frequencia)):
            # Compara as contagens (índice 1 de cada tupla)
            if lista_frequencia[i][1] < lista_frequencia[j][1]:
                # Troca as posições para colocar a maior contagem na frente
                lista_frequencia[i], lista_frequencia[j] = lista_frequencia[j], lista_frequencia[i]

    # A palavra mais frequente é sempre a primeira após a ordenação
    palavra_top = lista_frequencia[0][0]
    contagem_top = lista_frequencia[0][1]

# Rodando o programa

    print("\n=== Contagem de Palavras ===")

    # Percorre a lista ordenada e exibe cada par (palavra, contagem)
    for palavra, contagem in lista_frequencia:
        if contagem == 1:
            vezes = "vez"
        else:
            vezes = "vezes"

        # Formata a linha com a palavra entre aspas alinhada à esquerda
        print(f'"{palavra}"'.ljust(12) + f"-> {contagem} {vezes}")

    # Exibe o rodapé com a palavra mais frequente e total de únicas
    print(f'\nPalavra mais frequente: "{palavra_top}" ({contagem_top} vezes)')
    print(f"Total de palavras únicas: {len(frequencia)}")
