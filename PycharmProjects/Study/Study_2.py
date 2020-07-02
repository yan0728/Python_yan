import string

path = 'E:\python\Walden_new.txt'
with open(path,'r',encoding= 'utf-8') as text:
    words = [raw_word.strip(string.punctuation).lower() for raw_word in text.read().split()]
    # print(words)
    index_word = set(words)
    # print(index_word)
    words_dic = {index:words.count(index) for index in index_word}
    for word in sorted(words_dic,key=lambda x:words_dic[x],reverse = True):
        print(word + "  总共有"+str(words_dic[word])+'个')



