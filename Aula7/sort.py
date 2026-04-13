# 0 1 2 3
# 1 
# 2
# 3 

# lista[x][y]

# controlo de fluxo a uma dimensão
listanum = [9,2,4,8,6,1]
#index   =  0 1 2 3 4 5

# varaux = 1
# varaux = listanum[5]

# listanum[5] = 9
# listanum[5] = listanum[0]

# listanum[0] = 1
# listanum[0] = varaux

flags = True

#bubble sort
while flags:
    flags=False
    for i in range(len(listanum)-1):
        print(listanum)
        print("i =", i)
        if listanum[i] > listanum[i+1]:
            flags=True
            print("Troca aconteceu","posição i",listanum[i], "posição i+1", listanum[i+1])
            listanum[i], listanum[i+1] = listanum[i+1], listanum[i]

    print(listanum)





