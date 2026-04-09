class Exercicio2:
    """Algoritmo que analisa a viabilidade de um crédito financeiro"""
    
    def analisar_credito(self):
        salario_bruto = float(input("Digite o sálario bruto (R$): "))
        parcela = float(input("Digite o valor mensal da parcela desejada (R$): "))

        if parcela <= 0.20 * salario_bruto:
            porcentagem = (parcela / salario_bruto) * 100
            print(f"Salário bruto (R$): {salario_bruto}")
            print(f"Valor da parcela (R$): {parcela}")
            print(f"Comprometimento de renda (%): {porcentagem}%")
            print("SOLICITAÇÃO APROVADA: O valor está dentro do limite permitido")
        else:
            porcentagem = (parcela / salario_bruto) * 100
            print(f"Salário bruto (R$): {salario_bruto}")
            print(f"Valor da parcela (R$): {parcela}")
            print(f"Comprometimento de renda (%): {porcentagem}%")
            print(f"SOLICITAÇÃO NEGADA: A prestação excede 20% do salário")



if __name__ == "__main__":
    exercicio = Exercicio2()
    exercicio.analisar_credito()