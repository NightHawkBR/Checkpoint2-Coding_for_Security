# Lista inicial para teste:
# ips = ["192.168.1.1", "10.0.0.5", "172.16.0.3"]

# Sequência de teste:
# [1] Adicionar: "192.168.1.10" → "IP adicionado!"
# [1] Adicionar: "10.0.0.5"    → "IP já existe na lista!"
# [4] Buscar: "172.16.0.3"     → "IP encontrado na posição 3"
# [4] Buscar: "8.8.8.8"        → "IP não encontrado"
# [2] Remover: "10.0.0.5"      → "IP removido!"
# [3] Listar                   → exibe todos os IPs numerados
# [5] Sair                     → "Encerrando..."

# Lista que armazenará os endereços IP cadastrados
lista_ips = []

# Definindo loop com while
while True:
    
    print("---| GERENCIADOR DE IPs |---")
    print("---| [1] Adicionar IP   |---")
    print("---| [2] Remover IP     |---")
    print("---| [3] Listar todos   |---")
    print("---| [4] Buscar IP      |---")
    print("---| [5] Sair           |---")

    # Lê a opção digitada pelo usuário
    opcao = input("Escolha uma opção: ")

    # Opção 1: Adicionar IP
    if opcao == "1":
        ip = input("Digite o endereço IP: ")

        # Verifica se o IP já existe na lista
        if ip in lista_ips:
            print(f"Erro: o IP '{ip}' já está cadastrado.")
        else:
            lista_ips.append(ip)
            print(f"IP '{ip}' adicionado com sucesso!")

    # Opçaõ 2: Remover IP
    elif opcao == "2":
        ip = input("Digite o endereço IP a remover: ")
        if ip in lista_ips:
            lista_ips.remove(ip)
            print(f"IP '{ip}' removido com sucesso!")
        else:
            print(f"Erro: o IP '{ip}' não foi encontrado na lista.")

    # Opção 3: Listar todos
    elif opcao == "3":
        if not lista_ips:
            print("A lista está vazia.")
        else:
            print(f"IPs cadastrados ({len(lista_ips)} no total):")

            # enumerate() retorna o índice e o valor de cada item
            for indice, ip in enumerate(lista_ips, start=1): # start=1 faz a contagem começar em 1 (mais legível)
                print(f"  {indice}. {ip}")

    # Opção 4: Buscar IP
    elif opcao == "4":
        ip = input("Digite o endereço IP a buscar: ")
        if ip in lista_ips:
            # index() retorna a posição do item na lista (começa em 0)
            posicao = lista_ips.index(ip) + 1 # Soma-se 1 para exibir uma posição mais intuitiva ao usuário
            print(f"IP '{ip}' encontrado na posição {posicao}.")
        else:
            print(f"IP '{ip}' não encontrado na lista.")

    # Opção 5: Sair
    elif opcao == "5":
        print("Encerrando o programa. Até logo!")
        break

    # Em caso de opção inválida
    else:
        print("Opção inválida! Digite um número entre 1 e 5.")
