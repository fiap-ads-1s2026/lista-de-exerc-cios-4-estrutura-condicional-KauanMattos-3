class Exercicio3:
    """Algoritmo que calcula o desempenho acadêmico com média ponderada"""
    
    def calcular_desempenho_academico(self):

        n1 = float(input("Digite a nota da sua primeira avaliação (peso 1): "))
        n2 = float(input("Digite a nota da sua segunda avaliação (peso 1): "))
        n3 = float(input("Digite a nota da sua terceira avaliação (peso 2): "))
        media = (n1 + n2 + (n3 * 2)) / 4

        if media >= 6:
            print(f"Média Final: {media:.1f}")
            print("Status: APROVADO")
        else:
            print(f"Média Final: {media:.1f}")
            print("Status: REPROVADO")


if __name__ == "__main__":
    exercicio = Exercicio3()
    exercicio.calcular_desempenho_academico()