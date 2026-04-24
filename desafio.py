import random

# Dados iniciais:
senhas ={
    "gmail": "MinhaS3nha!",
    "github": "Dev@2024Seguro",
    "banco_dados": "db123"
}

# Caracteres para ingeção aleatória:
caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*"

def avaliar_forca(senha):
    """Avalia a força da senha usando um loop 'for' para verificar os critérios."""
    if len(senha) < 8:
        return "Fraca"
    
    tem_maiuscula = False
    tem_minuscula = False
    tem_numero = False
    tem_especial = False
    
    # Percorrendo a senha com 'for' como exigido
    for char in senha:
        if char.isupper():
            tem_maiuscula = True
        elif char.islower():
            tem_minuscula = True
        elif char.isdigit():
            tem_numero = True
        else:
            # Se não for letra nem número, é considerado especial
            tem_especial = True
            
    # Classificação com base nos booleanos
    if tem_maiuscula and tem_minuscula and tem_numero and tem_especial:
        return "Forte"
    elif (tem_maiuscula or tem_minuscula) and tem_numero and not tem_especial:
        return "Média"
    else:
        return "Fraca"

# Loop principal do programa
while True:
    print("\n" + "="*40)
    print("SISTEMA DE GERENCIAMENTO DE SENHAS")
    print("="*40)
    print("[1] Cadastrar senha")
    print("[2] Listar serviços")
    print("[3] Buscar senha por serviço")
    print("[4] Gerar senha aleatória")
    print("[5] Avaliar força de todas as senhas")
    print("[6] Exportar relatório")
    print("[7] Sair")
    
    # Tratamento de entrada inválida no menu com try/except
    try:
        opcao = int(input("\nEscolha uma opção: "))
    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite um número de 1 a 7.")
        continue

    if opcao == 1:
        servico = input("Digite o nome do serviço: ").strip().lower()
        
        if servico in senhas:
            print("Erro: Serviço já cadastrado!")
        else:
            senha_nova = input("Digite a senha: ")
            senhas[servico] = senha_nova
            forca = avaliar_forca(senha_nova)
            print(f"Cadastrado! Força: {forca}")

    elif opcao == 2:
        print("\nServiços cadastrados:")
        for s in senhas.keys():
            print(f"- {s}")

    elif opcao == 3:
        servico = input("Digite o nome do serviço para buscar a senha: ").strip().lower()
        if servico in senhas:
            print(f"Senha de '{servico}': {senhas[servico]}")
        else:
            print("Erro: Serviço não encontrado.")

    elif opcao == 4:
        try:
            tamanho = int(input("Digite o tamanho da senha (ex: 16): "))
            if tamanho <= 0:
                print("Erro: O tamanho deve ser maior que zero.")
                continue
            
            senha_gerada = ""
            # Gerando senha com for + random.choice
            for _ in range(tamanho):
                senha_gerada += random.choice(caracteres)
                
            print(f"Senha gerada aleatoriamente: {senha_gerada}")
        except ValueError:
            print("Erro: Entrada inválida. Digite um número inteiro para o tamanho.")

    elif opcao == 5:
        print("\nAvaliação de todas as senhas:")
        # Avaliando percorrendo o dicionário com for
        for servico, senha_cadastrada in senhas.items():
            forca = avaliar_forca(senha_cadastrada)
            print(f"{servico}:\t\"{senha_cadastrada}\"\t-> {forca}")

    elif opcao == 6:
        # Exportar relatório com try/except para erros de arquivo
        try:
            with open("senhas_relatorio.txt", "w", encoding="utf-8") as arquivo:
                arquivo.write("RELATÓRIO DE SENHAS\n")
                arquivo.write("-" * 30 + "\n")
                for servico, senha_cadastrada in senhas.items():
                    forca = avaliar_forca(senha_cadastrada)
                    arquivo.write(f"Serviço: {servico} | Senha: {senha_cadastrada} | Força: {forca}\n")
            print("Relatório exportado com sucesso!")
        except Exception as e:
            print(f"Erro ao exportar: [{e}]")

    elif opcao == 7:
        print("Encerrando...")
        break

    else:
        print("Erro: Opção inválida! Escolha um número de 1 a 7.")
