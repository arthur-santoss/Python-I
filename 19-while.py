gameName = input('digite o nome do jogo: ')

qtdRating = 0
totalRating = 0
rating = 0
average = 0 

while (rating != -1):
    rating = float(input("Informe a nota do jogo: "))
    if(rating != -1):
        totalRating += rating
        qtdRating += 1
        average = totalRating / qtdRating
print(f"Média do jogo {gameName} é {average:.2f}")   