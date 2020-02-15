#Função de tratamento de erro do menu
def tratarMenu(msg):
    try:
        opcao = int(input(msg))
        if opcao > 0 and opcao <= 7:
            return opcao
        else:
            print("Informação invalida, digite uma opção entre 1 e 7")
            return tratarMenu(msg)
    except:
        print("Informação invalida, digite uma opção entre 1 e 7")
        return tratarMenu(msg)