def pokolenia(tab):
    wyniki = [ [ tab[0][0] ],[ tab[0][1] ] ]
    tab.pop(0)
    
    while len(tab)>0:
        i = 0
        while i < len(tab):
            for j in range(len(wyniki)):
                #print(tab[i], '    ', wyniki[j])
                if tab[i][0] in wyniki[j]:
                    if j < len(wyniki)-1:
                        wyniki[j+1].append(tab[i][1])
                    else:
                        wyniki.append([tab[i][1]])
                    tab.pop(i)
                    i = 0
                    break

                elif tab[i][1] in wyniki[j]:
                    if j > 0:
                        wyniki[j-1].append(tab[i][0])
                    else:
                        wyniki.insert(0,[tab[i][0]])
                    tab.pop(i)
                    i = 0
                    break

                
            i+=1

    for pokolenie in wyniki:
        pokolenie.sort()


    
    wyniki[0] = wyniki[0][0]



    return wyniki

print( pokolenia([['Z', 'D'], ['A', 'B'], ['F','B'],['B','C'],['C','D'],['D','F']])  )
#print( pokolenia([["a","b"],["b","x"],["a","d"],["a","z"]]) )
#print( pokolenia([["Ula", "Ala"], ["Ola", "Ula"], ["Ela", "Ola"], ["Ela", "Jan"]]) )
