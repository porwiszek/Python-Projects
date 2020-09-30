def spliting(string):
    li = len(list(string.split(" ")))
    return li

abc = "Geeks for Geeks"
print(spliting(abc))

def count_words(strng): 
    strng_list = strng.split() 
    return len(strng_list) 
     
print(count_words("Hey there it's me!"))