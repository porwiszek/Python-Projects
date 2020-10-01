def external_word_count(string):
    file = open(string, "rt")
    data = file.read()
    words = data.split()
    return len(words)
    
path = "words1.txt"
print('Number of words in text file :', external_word_count(path))

def external_word_count2(string2):
    with open(string2 , "r") as file:
        data = file.read()
        words = data.split()
        return len(words)

print('Number of words in text file :', external_word_count2(path))

import math
print(math.cos(1))

import math
print(math.pow(2,2))

for letter in "Hello":
    if letter == "e":
        print(letter)

def external_word_count2(string2):
    with open(string2 , 'r') as file:
        data = file.read()
    data = data.replace(",", " ")
    string_list = data.split(" ")
    return len(string_list)

path2 = "words2.txt"

print('Number of words in second text file :', external_word_count2(path2))

import re
     
def count_words_re(filepath):
    with open(filepath, 'r') as file:
        text = file.read()
    string_list = re.split(",| ", text)
    return len(string_list)
     
print(count_words_re("words2.txt"))


import string
outF = open("myOutFile.txt", "w")
for x in string.ascii_lowercase:
    outF.write(x)
    outF.write("\n")
outF.close()

#using as file automaticaly close file
outF2 = open("myOutFile2.txt", "w")
for x in string.ascii_lowercase:
    outF2.write(x + "\n")