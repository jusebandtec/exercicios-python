def soma_imposto(taxa_imposto, custo):
    porcentagem = taxa_imposto/100
    custo = custo - (custo*porcentagem)
    return custo

print(soma_imposto(30, 100))