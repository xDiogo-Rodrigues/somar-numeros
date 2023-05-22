from funcoes import criar_funcao, somar

list_numbers = [10,25,50,100]

sum_numbers = criar_funcao(somar,*list_numbers)

print(sum_numbers())