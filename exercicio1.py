# Teste com estas frases:
# testes = [
#    "Python para Seguranca",
#    "Hello World 123!",
#    "aeiou",
#    "",
# ]

# Definindo vogais e consoantes
vogais = ("a","e","i","o","u")
consoantes = ('b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z')

#Pedindo frase ao usuário
print("---Contador de letras---")
frase = input("Digite uma frase: ").lower()

#Contador de vogais e consoantes
numero_vogais = 0 
numero_consoantes = 0

#Criando o loop
for letra in frase:
    if letra in vogais: 
        numero_vogais += 1

    if letra in consoantes: 
        numero_consoantes += 1

#Saída do programa
print(f"Vogais: {numero_vogais}")
print(f"Consoantes: {numero_consoantes}")
