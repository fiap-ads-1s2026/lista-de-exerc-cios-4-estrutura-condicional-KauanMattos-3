class Exercicio7:
    """Algoritmo que solicita a idade de um nadador e imprime sua categoria"""
    
    def categorizar_nadador(self):
         
         idade = int(input("\nDigite a idade do nadador: "))
         infatil = 5 <= idade <= 10
         juvenil = 11 <= idade <= 17
         senior = idade >= 18

         if infatil:
             print(f"\nIdade informada: {idade} anos")
             print("INFANTIL")
             print("Faixa etária: 5 a 10 anos\n")

         elif juvenil:
             print(f"\nIdade informada: {idade} anos")
             print("JUVENIL")
             print("Faixa etária: 11 a 17 anos\n")

         elif senior:
             print(f"\nIdade informada: {idade} anos")
             print("SÊNIOR")
             print("Faixa etária: 18 anos ou mais\n")

         else:
             print(f"\nIdade informada: {idade} anos")
             print("Categoria: O atleta não possui categoria definida")
             print("Motivo: Idade inferior a 5 anos\n")




if __name__ == "__main__":
    exercicio = Exercicio7()
    exercicio.categorizar_nadador()