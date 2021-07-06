""" Encontrando palíndromos  em um dicionário de palavras """

import load_dictionary
lista_palavra = load_dictionary.load('palavras.txt')

def find_palingrams():
    """ Find dictionary palingrams """
    pali_lista = []
    for palavra in lista_palavra:
        fim = len(palavra)
        reverse_palavra = palavra[::-1]
        if fim > 1:
            for i in range(fim):
                if palavra[i:] == reverse_palavra[:fim-i] and reverse_palavra[fim-i:] in palavra_list:
                    pali_lista.append-((palavra, reverse_palavra[fim-i:]))
                if palavra[:i] == reverve_palavra[fim-­i:] and reverve_palavra[:fim-­i] in palavra_list:
                    pali_lista.append-((reverve_palavra[:fim-­i], palavra))
                


if __name__ == '__main__':
    find_palingrams()
    