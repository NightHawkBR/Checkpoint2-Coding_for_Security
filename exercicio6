# Set com os IPs que acessaram o servidor
acessos = {"192.168.1.10", "10.0.0.5", "185.220.101.1", "172.16.0.3",
           "192.168.1.20", "91.240.118.172", "10.0.0.12", "45.33.32.156"}

# Set com os IPs considerados maliciosos (blacklist)
blacklist = {"185.220.101.1", "45.33.32.156", "91.240.118.172",
             "23.94.5.100", "104.244.72.115"}

# IPs maliciosos que realmente acessaram o servidor
maliciosos_detectados = acessos & blacklist

# IPs que acessaram e são considerados seguros
ips_seguros = acessos - blacklist

# IPs maliciosos que constam na blacklist mas não tentaram acesso
blacklist_nao_detectados = blacklist - acessos

# Total de IPs distintos entre acessos e blacklist
todos_ips = acessos | blacklist

# Rodando o programa

print("=== Relatório de Segurança ===")

# Exibe os IPs maliciosos detectados (interseção)
print(f"\nIPs maliciosos detectados ({len(maliciosos_detectados)}):")
for ip in maliciosos_detectados:
    print(f"   - {ip}")

# Exibe os IPs seguros (diferença acessos - blacklist)
print(f"\nIPs seguros ({len(ips_seguros)}):")
for ip in ips_seguros:
    print(f"   - {ip}")

# Exibe os IPs da blacklist que não apareceram nos acessos (diferença inversa)
print(f"\nIPs da blacklist não detectados ({len(blacklist_nao_detectados)}):")
for ip in blacklist_nao_detectados:
    print(f"   - {ip}")

# Exibe o total de IPs únicos considerando ambas as listas (união)
print(f"\nTotal de IPs únicos: {len(todos_ips)}")
