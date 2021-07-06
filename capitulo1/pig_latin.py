'''
Input a word and return a Pig Latin game
'''

def main():
    '''recebendo a palavra no input e convertendo a strig no jogo pig latin'''
    word = input("Digite a palavra: ")
    if word is not None:
        fist_letter= word[0]
        rest_letter= word[1:]
        print(rest_letter + fist_letter +'ay')



if __name__ == '__main__':
    main()
