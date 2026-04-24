# Teste com estas senhas:
# testes = [
#   "abc",              # Fraca: faltam maiúscula, número, especial, < 8 chars
#   "abcdefgh",         # Faltam maiúscula, número, especial
#   "Abcdefgh",         # Faltam número e especial
#   "Abcdefg1",         # Falta especial
#   "Cyber@2024",       # Válida!
# ]

# Conjunto de caracteres especiais permitidos em maiúsculas para indicar uma constante
CARACTERES_ESPECIAIS = "!@#$%&*"  

#Definido loop com while
while True:
    senha = input("Digite uma senha: ")

    #Lista que armazena os problemas da senha
    problemas = []

    #Critérios para criar uma senha válida
    if len(senha) < 8:
        problemas.append("- Falta pelo menos 8 caracteres")

    if not any(c.isupper() for c in senha): #any() percorre cada caratcere em busca de maiusculos
        problemas.append("Falta pelo menos 1 letra maiúscula")

    if not any(c.isdigit() for c in senha):
        problemas.append("Falta pelo menos 1 número")

    if not any(c in CARACTERES_ESPECIAIS for c in senha):
        problemas.append(f"Falta pelo menos 1 caractere especial ({CARACTERES_ESPECIAIS})")
    
    #Estando tudo certo
    if not problemas: 
        print("Senha Válida!")
        break
    
    #Se houver problemas, exibe e lista cada um deles.
    print("Senha inválida! Problemas encontados: ")
    for problema in problemas:
        print(problema)

    print("Digite outra senha")
