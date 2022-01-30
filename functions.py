import docx
from spellchecker import SpellChecker
import unicodedata
import re
import pandas as pd
import re
# https://stackoverflow.com/questions/919056/case-insensitive-replace
# getting text from docx file
def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return ' '.join(fullText)


def re_replace(sentence, og_word, rpl_word):

    insensitive_replace = re.compile(re.escape(og_word), re.IGNORECASE)
    insensitive_replace.sub(rpl_word, sentence)
    return insensitive_replace.sub(rpl_word, sentence)

# sample line of code
# re_replace("I want a hIPpo for my birthday", 'hippo', 'lion')


def paragraph_replace(text, dictionary):
    keys_list = list(dictionary.keys())
    vals_list = list(dictionary.values())
    final_string = text
    for key, val in zip(keys_list, vals_list):
        temp_string = re_replace(final_string, key, val)
        final_string = temp_string
#     print(final_string)
    return final_string


def to_dictionary(list1, list2):
    test_keys = list1
    test_values = list2

    # # Printing original keys-value lists
    # print ("Original key list is : " + str(test_keys))
    # print("")
    # print ("Original value list is : " + str(test_values))

    # using naive method
    # to convert lists to dictionary
    res = {}
    for key in test_keys:
        for value in test_values:
            res[key] = value
            test_values.remove(value)
            break

    # # Printing resultant dictionary
    # print(" ")
    # print ("Resultant dictionary is : " +  str(res))
#     diacritic_dictionary = res
    return res
