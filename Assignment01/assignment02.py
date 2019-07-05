# 有bug

import re
import jieba
from collections import Counter

filename = '/Users/nobo/Downloads/movie_comments.csv'
comment = ""
TOKEN = []

def cut(string): return list(jieba.cut(string))

for i in open(filename).readlines():
    try:
        j = i.strip("\n").split(",")[3]
        comment = comment + ''.join(re.findall('\w+', j))
    except:
        pass

TOKEN = jieba.cut(comment)

words_count = Counter(TOKEN)

TOKEN_2_GRAM = [''.join(TOKEN[i:i+2]) for i in range(len(TOKEN[:-2]))]

def prob_2(word1, word2):
    if word1 + word2 in words_count_2: return words_count_2[word1+word2] / len(TOKEN_2_GRAM)
    else:
        return 1 / len(TOKEN_2_GRAM)


def get_probablity(sentence):
    words = cut(sentence)
    sentence_pro = 1
    for i, word in enumerate(words[:-1]):
        next_ = words[i + 1]
        probability = prob_2(word, next_)
        sentence_pro *= probability
    return sentence_pro

