# Sequência de teste:
# Número 1: abc     → "Erro: Digite apenas números!"
# Número 1: 10
# Número 2: 0
# Operação: /       → "Erro: Divisão por zero!"
# Número 1: 10
# Número 2: 3
# Operação: /       → "Resultado: 3.33"
# Número 1: 5
# Número 2: 3
# Operação: %       → "Erro: Operação '%' não suportada. Use +, -, * ou /"
# Número 1: sair    → "Encerrando calculadora."

# Cada interação deve exibir ao final:
# "Operação processada." (via finally)

print("---| CALCULADORA SEGURA |---")
print('Digite "sair" para encerrar.')

# Definindo loop while para manter a calculadora ativa até o usuário digitar "sair"
while True:

    # Todas as leituras ficam DENTRO do try para garantir que o finally
    # sempre execute "Operação processada.", inclusive no "sair"
    try:
        entrada1 = input("Número 1: ")

        # Verifica se o usuário quer encerrar o programa
        if entrada1.lower() == "sair":
            print("Encerrando calculadora.")
            break

        entrada2 = input("Número 2: ")

        if entrada2.lower() == "sair":
            print("Encerrando calculadora.")
            break

        # Realizando as operações
        operacao = input("Operação (+,-,*,/): ")

        if operacao.lower() == "sair":
            print("Encerrando calculadora.")
            break

        # Tenta converter as entradas para float
        num1 = float(entrada1)
        num2 = float(entrada2)

        # Verifica se a operação digitada é válida
        # O raise interrompe o try e vai direto para o except ValueError
        if operacao not in ("+", "-", "*", "/"):
            raise ValueError(f"Operação '{operacao}' não suportada. Use +, -, * ou /")

        # Executa a operação escolhida
        if operacao == "+":
            resultado = num1 + num2

        elif operacao == "-":
            resultado = num1 - num2

        elif operacao == "*":
            resultado = num1 * num2

        elif operacao == "/":
            resultado = num1 / num2

    except ValueError:
        # Captura: entrada não numérica OU operação inválida
        if not entrada1.replace(".", "").replace("-", "").isdigit():
            print("Erro: Digite apenas números!")
        elif not entrada2.replace(".", "").replace("-", "").isdigit():
            print("Erro: Digite apenas números!")
        else:
            print(f"Erro: Operação '{operacao}' não suportada. Use +, -, * ou /")

    except ZeroDivisionError:
        print("Erro: Divisão por zero!")

    else:
        # Executado SOMENTE quando nenhuma exceção foi lançada
        print(f"Resultado: {resultado:.2f}".rstrip("0").rstrip("."))

    finally:
        # Executado SEMPRE, com ou sem erro — inclusive no "sair"
        print("Operação processada.")
