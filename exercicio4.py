class Exercicio4:
    """Algoritmo que apresenta um menu interativo com operações aritméticas"""

    def menu_calculadora(self):

        print("==== CALCULADORA ====")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")

        opcao = int(input("Escolha uma opção (1-5): "))

        if opcao == 1:
            n1 = int(input("Digite o primeiro número: ")) 
            n2 = int(input("Digite o segundo número: "))
            resultado = n1 + n2
            print(f"Resultado = {n1} + {n2} = {resultado}")

        elif opcao == 2:
            n1 = int(input("Digite o primeiro número: ")) 
            n2 = int(input("Digite o segundo número: "))
            resultado = n1 - n2
            print(f"Resultado = {n1} - {n2} = {resultado}")

        elif opcao == 3:
            n1 = int(input("Digite o primeiro número: ")) 
            n2 = int(input("Digite o segundo número: "))
            resultado = n1 * n2
            print(f"Resultado = {n1} * {n2} = {resultado}")

        elif opcao == 4:
            n1 = int(input("Digite o primeiro número: ")) 
            n2 = int(input("Digite o segundo número: "))
        
            if n2 == 0:
                print("ERRO: Divisão por zero não é permitida!")

            else: 
                resultado = n1 / n2
                print(f"Resultado = {n1} / {n2} = {resultado}")

        elif opcao == 5:
            print(f"Desligando a calculadora...")
        else:
            print("Opção Inválida - Tente novamente")

if __name__ == "__main__":
    exercicio = Exercicio4()
    exercicio.menu_calculadora()