# import requests
# import json
# import re
# import random
# import pprint
# # Distractors from http://conceptnet.io/


# def get_distractors_conceptnet(word):
#     word = word.lower()
#     original_word = word
#     if (len(word.split()) > 0):
#         word = word.replace(" ", "_")
#     distractor_list = []
#     url = "http://api.conceptnet.io/query?node=/c/en/%s/n&rel=/r/PartOf&start=/c/en/%s&limit=5" % (
#         word, word)
#     obj = requests.get(url).json()

#     for edge in obj['edges']:
#         link = edge['end']['term']

#         url2 = "http://api.conceptnet.io/query?node=%s&rel=/r/PartOf&end=%s&limit=10" % (
#             link, link)
#         obj2 = requests.get(url2).json()
#         for edge in obj2['edges']:
#             word2 = edge['start']['label']
#             if word2 not in distractor_list and original_word.lower() not in word2.lower():
#                 distractor_list.append(word2)

#     return distractor_list


# original_word = "One Day International"
# distractors = get_distractors_conceptnet(original_word)

# print("Original word: ", original_word)
# print("\nDistractors ", distractors)

from collections import OrderedDict

# load sense2vec vectors
from sense2vec import Sense2Vec
s2v = Sense2Vec().from_disk('s2v_old')


def sense2vec_get_words(word, s2v):
    output = []
    word = word.lower()
    word = word.replace(" ", "_")

    sense = s2v.get_best_sense(word)
    most_similar = s2v.most_similar(sense, n=3)

    # print ("most_similar ",most_similar)

    for each_word in most_similar:
        append_word = each_word[0].split("|")[0].replace("_", " ").lower()
        if append_word.lower() != word:
            output.append(append_word.title())

    out = list(OrderedDict.fromkeys(output))
    return out


word = "One Day International"
distractors = sense2vec_get_words(word, s2v)

print("Distractors for ", word, " : ")
print(distractors)
