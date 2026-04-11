class Exercicio5:
    """Algoritmo que realiza verificação previdenciária"""
    
    def verificar_aposentadoria(self):

        idade = int(input("Digite a idade cronológica (anos): "))
        tempo = int(input("Digite o tempo de contribuição (anos): "))

        idade_ok = idade >= 65
        tempo_ok = tempo >= 30
        misto_ok = idade >= 60 and tempo >= 25

        print("Dados do Colaborador:")
        print(f"Idade: {idade} anos")
        print(f"Tempo de contribuição: {tempo} anos")

        print("Análise dos critérios:")

        if idade_ok:
            print("• Critério por Idade:  ✓  ATENDE")
        else:
            print(f"• Critério por Idade: ✗ NÃO ATENDE")

        if tempo_ok:
            print(f"• Critério por Tempo: ✓  ATENDE")
        else:
            print(f"• Critério por Tempo: ✗ NÃO ATENDE")

        if misto_ok:
            print("• Critério Misto: ✓ ATENDE")
        else:
            print("• Critério Misto: ✗ NÃO ATENDE")

        if idade_ok or tempo_ok or misto_ok:
            print("PARECER: O trabalhador ESTÁ APTO para aposentadoria")
        else:
            print("PARECER: O trabalhador NÃO ESTÁ APTO para aposentadoria")
            print("Para se aposentar, é necessário atender pelo menos um dos critérios:")
            print(f"Completar 7 anos para atingir 65")
            print(f"Contribuir por mais de 10 anos para atingir 30")
            print(f"Ou atingir 60 anos de idade e 25 anos de contribuição")




if __name__ == "__main__":
    exercicio = Exercicio5()
    exercicio.verificar_aposentadoria()