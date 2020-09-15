def busca_ordenhadas(ordenhadas, i):
    e = 0
    d = len(ordenhadas) - 1

    while e <= d:

        meio = (e + d) // 2

        if ordenhadas[meio] == vaca:
            return meio
        elif vaca < ordenhadas[meio]:
            d = meio - 1
        elif vaca > meio:
            e = meio + 1

    return -1  # se a vaca não foi localizada

# entra com a lista das vacas já ordenhadas
lista = input("Entre com os códigos das vacas já ordenhadas, separados "
              "por espaços: ")

# ordena e converte de string para int a lista original para iniciar
# a verificação
ordenha = sorted([int(v) for v in lista.split()])

# vaca a ser verificada
vaca = int(input("Vaca a ser verificada: "))

localizacao = busca_ordenhadas(ordenha, vaca)

if localizacao == -1:
    print("Vaca não ordenhada.")
else:
    print('A vaca {0} foi ordenhada e se encontra na posição {1}.'
          .format(vaca, localizacao))

print('Lista das vacas já ordenhadas: {0}'.format(ordenha))
