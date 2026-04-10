class Exercicio1:
    """Algoritmo que receba duas notas escolares e calcule a média aritmética"""
    
    def calcular_media_notas(self):
        n1 = float(input("Digite a sua primeira nota (0.0 a 10.0): "))
        n2 = float(input("Digite a sua segunda nota (0.0 a 10.0): "))

        # Validação
        if n1 > 10 or n2 > 10 or n1 < 0 or n2 < 0:
            print("ERRO: As notas devem estar no intervalo de 0.0 a 10.0")
            return # Encerra o método
        
        # Cálculo
        else:
            media = (n1 + n2) / 2

        # Saída
        print(f"Nota 1: {n1:.2f}")
        print(f"Nota 2: {n2:.2f}")
        print(f"Média aritmética: {media:.1f}")
    

if __name__ == "__main__":
    exercicio = Exercicio1()
    exercicio.calcular_media_notas()

