import load_file

w_list = load_file.load('words.txt')

anagram_list = []

name = input('Input name: ')
name = name.lower()
name_sorted = sorted(name)
print(name_sorted)
print(w_list)

for word in w_list:
    word = word.lower()
    if word != name:
        if sorted(word) == name_sorted:
            anagram_list.append(word)
    if len(anagram_list) == 0:
        print("Precisa de um  dicionário longo ou mais palavras")
        break
    else:
        print("Anagrams=", *anagram_list, sep='\n')
    


