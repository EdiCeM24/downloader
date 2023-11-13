search = "how to create a password generator using python python using algorithm"
words = search.split()
counts = {} #dictionary
count = 0

for i in range(0, len(words)):
    first_word = words[i]
    #print(first_word)
    for i in range(0, len(words)):
        second_word = words[i]
        if first_word == second_word:
            count = count + 1
    counts[first_word]= count 
    count = 0
print(counts)   
