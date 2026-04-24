# Lista de logs a serem analisados
logs = [
    "[2025-02-20 08:15:01] [INFO] Login ok - IP: 192.168.1.10",
    "[2025-02-20 08:15:03] [WARNING] Area restrita - IP: 10.0.0.5",
    "[2025-02-20 08:15:10] [ERROR] Falha auth - IP: 185.220.101.1",
    "[2025-02-20 08:15:15] [INFO] Arquivo acessado - IP: 192.168.1.10",
    "[2025-02-20 08:15:22] [ERROR] Conexao recusada - IP: 185.220.101.1",
    "[2025-02-20 08:15:30] [WARNING] Certificado SSL - IP: 172.16.0.3",
    "[2025-02-20 08:15:35] [ERROR] Falha auth - IP: 10.0.0.5",
    "log malformado sem formato correto",
    "[2025-02-20 08:15:45] [ERROR] Timeout - IP: 185.220.101.1",
    "[2025-02-20 08:15:50] [WARNING] CPU alta - IP: 192.168.1.20",
    "[2025-02-20 08:16:01] [ERROR] Falha auth - IP: 185.220.101.1",
    "[2025-02-20 08:16:05] [INFO] Firewall ok - IP: 192.168.1.10",
]

# Dicionário para contar eventos por nível (INFO, WARNING, ERROR)
contagem_niveis = {"INFO": 0, "WARNING": 0, "ERROR": 0}

# Dicionário para contar erros por IP: {ip: quantidade_de_erros}
erros_por_ip = {}

# Contador de logs malformados (que não seguem o formato esperado)
malformados = 0

# Processando os logs

# Percorre cada linha de log da lista
for log in logs:
    try:
        # Verifica se o log contém os marcadores esperados
        # Um log válido deve ter "[" no início e "IP:" no conteúdo
        if not log.startswith("[") or "IP:" not in log:
            raise ValueError("Formato de log inválido.")

        # Extrai o nível: busca o texto entre o segundo "[" e "]"
        parte_nivel = log.split("] [")[1]
        nivel = parte_nivel.split("]")[0]

        # Valida se o nível extraído é um dos esperados
        if nivel not in contagem_niveis:
            raise ValueError(f"Nível desconhecido: '{nivel}'")

        # Extrai o IP: pega tudo após "IP: " e remove espaços extras
        ip = log.split("IP: ")[1].strip()

        # Incrementa o contador do nível encontrado
        contagem_niveis[nivel] += 1

        # Se o nível for ERROR, registra o IP no dicionário de erros
        if nivel == "ERROR":
            # .get(ip, 0) retorna 0 se o IP ainda não existe no dicionário
            erros_por_ip[ip] = erros_por_ip.get(ip, 0) + 1

    except (ValueError, IndexError):
        malformados += 1

# Identificando IPs com mais erros
ip_mais_erros = None
maior_contagem = 0

for ip, contagem in erros_por_ip.items():
    if contagem > maior_contagem:
        maior_contagem = contagem
        ip_mais_erros  = ip

# Rodando o programa

print("=== Relatório de Logs ===")
print(f"INFO:    {contagem_niveis['INFO']} eventos")
print(f"WARNING: {contagem_niveis['WARNING']} eventos")
print(f"ERROR:   {contagem_niveis['ERROR']} eventos")
print(f"Logs malformados: {malformados}")

print(f"\nIP com mais erros: {ip_mais_erros} ({maior_contagem} erros)")

print("\nDetalhamento de erros:")
for ip, contagem in erros_por_ip.items():
    # Usa "erro" no singular se a contagem for 1, "erros" caso contrário
    erro_texto = "erro" if contagem == 1 else "erros"
    print(f"  {ip:<18} → {contagem} {erro_texto}")
