class Exercicio6:
    """Algoritmo que calcula o IMC e verifica se a pessoa está no peso ideal"""
    
    def calcular_imc(self):
         
         peso = float(input("\nDigite o peso em kg: "))
         altura = float(input("Digite a altura em metros: "))
         imc = peso / (altura * altura)

         print("\nDados informados:")
         print(f"Peso: {peso} kg")
         print(f"Altura: {altura} m")
    
         print(f"\nÍndice de Massa Corporal (IMC): {imc:.1f}")
         
         if 18.5 <= imc <= 24.9:
            print(f"Classificação: Peso normal")
            print(f"Status: ESTÁ no peso ideal ✓")

            print("Referência OMS - Peso ideal: IMC entre 18,5 e 24,9")
         else:
            print(f"Classificação: Obesidade")
            print(f"Status: NÃO está no peso ideal ✗")

            print("\nReferência OMS - Peso ideal: IMC entre 18,5 e 24,9\n")      
             


if __name__ == "__main__":
    exercicio = Exercicio6()
    exercicio.calcular_imc()