import random

#THIS IS A INFINITE LOOP, BE CAREFUL, IF YOU WANT TO STOP IN ONLY 1 LIST, CHANGE THE VALUE OF 1 TO 0
#ISSO É UM LOOP INFINITO, TOME CUIDADE, SE QUISER QUE SEJA SOMENTE 1 LISTA, MUDE O VALOR DE 1 PARA 0

#Your list of things \\ Lista de coisas
list = ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#Shuffling your list \\ Fazendo de sua lista aleatória
RandomList = random.sample(list, k=len(list))
#Calculating how many items do you have on the list \\ Calculando quantos items você tem na lista
LenRandomList = len(RandomList)
#Empty list to items already used \\ Lista vazia para armazenar items já utilizados
AlreadyPlayed = []
#Loop comparing how many items do you have to 0 \\ Loop calculando quantos itens tem comparado a 0
while LenRandomList > 0:
    #Loop adding to your "AlreadyPlayed" list and removing it from the random list \\ Loop adicionando para a lista já usada e removendo da lista random
    for item in RandomList:
        AlreadyPlayed.append(item)
        RandomList.remove(item)
        #Updating the quantity object \\ Atualizando o objeto de quantidade
        LenRandomList = len(RandomList)
        #Comparing the quantity of items in the list, if the lengh equals 1, it will update the RandomList to another one
        #Comparando a quantidade de itens na lista, se a quantidade for igual a 1 ela vai atualizar a RandomList para outra
        if LenRandomList == 1:
            RandomList = random.sample(list, k=len(list))
        print("Used List: ", AlreadyPlayed, "\n Removed List: ", RandomList)