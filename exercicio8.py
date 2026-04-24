# Tipos e status válidos para validação no cadastro
TIPOS_VALIDOS  = ("servidor", "estacao", "switch", "roteador")
STATUS_VALIDOS = ("ativo", "inativo")


# Classe Inventário
# Responsável por gerenciar a lista de dicionários e toda a lógica
class Inventario:

    # Método construtor: inicializa a lista com os dados iniciais
    def __init__(self):
        self.ativos = [
            {"nome": "SRV-WEB01", "tipo": "servidor", "ip": "192.168.1.10", "status": "ativo"},
            {"nome": "PC-RH03",   "tipo": "estacao",  "ip": "192.168.1.45", "status": "ativo"},
            {"nome": "SW-CORE01", "tipo": "switch",   "ip": "192.168.1.1",  "status": "inativo"},
        ]

    def buscar_por_ip(self, ip):
        #Percorre a lista de dicionários e retorna o ativo com o IP informado.
        for ativo in self.ativos:
            if ativo["ip"] == ip:
                return ativo
        return None

    def exibir_ativo(self, ativo, indice=None):
        #Exibe os dados de um dicionário de ativo formatado na tela.
        prefixo = f"  [{indice}]" if indice is not None else "  "
        print(f"{prefixo} Nome  : {ativo['nome']}")
        print(f"       Tipo  : {ativo['tipo']}")
        print(f"       IP    : {ativo['ip']}")
        print(f"       Status: {ativo['status']}")
        print()

    def cadastrar(self):
        #Solicita os dados do novo ativo e adiciona à lista como dicionário.
        print("\n--- Cadastrar Ativo ---")
        try:
            nome = input("Nome do ativo : ").strip()
            if not nome:
                raise ValueError("O nome não pode ser vazio.")

            tipo = input(f"Tipo {TIPOS_VALIDOS}: ").strip().lower()
            if tipo not in TIPOS_VALIDOS:
                raise ValueError(f"Tipo inválido. Use: {', '.join(TIPOS_VALIDOS)}")

            ip = input("Endereço IP   : ").strip()
            if self.buscar_por_ip(ip):
                raise ValueError(f"IP '{ip}' já está cadastrado.")

            status = input(f"Status {STATUS_VALIDOS}: ").strip().lower()
            if status not in STATUS_VALIDOS:
                raise ValueError(f"Status inválido. Use: {', '.join(STATUS_VALIDOS)}")

            # Cria o dicionário do novo ativo e adiciona à lista
            novo_ativo = {"nome": nome, "tipo": tipo, "ip": ip, "status": status}
            self.ativos.append(novo_ativo)
            print(f"\nAtivo '{nome}' cadastrado com sucesso!")

        except ValueError as erro:
            print(f"\nErro ao cadastrar: {erro}")

    def listar(self):
        #Percorre a lista e exibe todos os dicionários de ativos.
        print("\n--- Lista de Ativos ---")
        if not self.ativos:
            print("Nenhum ativo cadastrado.")
            return

        # enumerate() fornece o índice e o dicionário a cada iteração
        for indice, ativo in enumerate(self.ativos, start=1):
            self.exibir_ativo(ativo, indice)

    def buscar(self):
        #Busca um dicionário de ativo pelo IP e exibe seus dados.
        print("\n--- Buscar por IP ---")
        try:
            ip = input("Digite o IP   : ").strip()
            ativo = self.buscar_por_ip(ip)

            if not ativo:
                raise ValueError(f"Nenhum ativo encontrado com o IP '{ip}'.")

            print()
            self.exibir_ativo(ativo)

        except ValueError as erro:
            print(f"\nErro na busca: {erro}")

    def alterar_status(self):
        #Busca um ativo pelo IP e altera o valor 'status' no dicionário.
        print("\n--- Alterar Status ---")
        try:
            ip = input("IP do ativo   : ").strip()
            ativo = self.buscar_por_ip(ip)

            if not ativo:
                raise ValueError(f"Nenhum ativo encontrado com o IP '{ip}'.")

            print(f"Status atual  : {ativo['status']}")

            novo_status = input(f"Novo status {STATUS_VALIDOS}: ").strip().lower()
            if novo_status not in STATUS_VALIDOS:
                raise ValueError(f"Status inválido. Use: {', '.join(STATUS_VALIDOS)}")

            # Atualiza o valor da chave 'status' no dicionário
            ativo["status"] = novo_status
            print(f"\nStatus de '{ativo['nome']}' alterado para '{novo_status}'.")

        except ValueError as erro:
            print(f"\nErro ao alterar: {erro}")

    def remover(self):
        #Busca um ativo pelo IP e remove o dicionário da lista.
        print("\n--- Remover Ativo ---")
        try:
            ip = input("IP do ativo   : ").strip()
            ativo = self.buscar_por_ip(ip)

            if not ativo:
                raise ValueError(f"Nenhum ativo encontrado com o IP '{ip}'.")

            self.ativos.remove(ativo)
            print(f"\nAtivo '{ativo['nome']}' removido com sucesso!")

        except ValueError as erro:
            print(f"\nErro ao remover: {erro}")


# Classe Menu
# Responsável pela interface de interação com o usuário
class Menu:

    # Método construtor: recebe o inventário como dependência
    def __init__(self, inventario):
        self.inventario = inventario

    def exibir(self):
        #Exibe as opções do menu na tela.
        print("=" * 35)
        print("   INVENTÁRIO DE ATIVOS DE REDE")
        print("=" * 35)
        print("  [1] Cadastrar ativo")
        print("  [2] Listar ativos")
        print("  [3] Buscar por IP")
        print("  [4] Alterar status")
        print("  [5] Remover ativo")
        print("  [6] Sair")
        print("=" * 35)

    def executar(self):
        #Executa o loop principal do menu.
        while True:
            self.exibir()
            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                self.inventario.cadastrar()
            elif opcao == "2":
                self.inventario.listar()
            elif opcao == "3":
                self.inventario.buscar()
            elif opcao == "4":
                self.inventario.alterar_status()
            elif opcao == "5":
                self.inventario.remover()
            elif opcao == "6":
                print("Encerrando o sistema. Até logo!")
                break
            else:
                print("Opção inválida! Digite um número entre 1 e 6.")


# Rodando o programa
# Cria o inventário (dados como dicionários + lógica)
inventario = Inventario()

# Cria o menu passando o inventário como dependência
menu = Menu(inventario)

# Inicia o loop do menu
menu.executar()
