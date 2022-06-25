def somar():
    lista = []
    for x in range(5):
        lista.append(int(input()))
        # print(lista[:])
    
    # print(lista)
    return sum(lista)

def main():
    
    somar()
    # f = open("6.in", "r")
    # arquivo = f.read()
    # arquivo = arquivo.split("\n")
    # arquivo = map(lambda x: int(x), arquivo)
    # arquivo = list(arquivo)
    # print(arquivo)
    


if __name__ == '__main__':
    main()