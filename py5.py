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