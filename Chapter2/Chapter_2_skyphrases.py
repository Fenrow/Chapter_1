"""
Chapter 2 "Skyphrases"
"""

filename = 'skychallenge_skyphrase_input.txt'
valid = 0
nv =0
with open(filename) as f:
    content = f.read().splitlines()

for line in content:                                        #Check line by line
    spaces = []                                             #List of spaces between words
    for char in range(0, len(line)):
        if line[char] == ' ':
            spaces.append(char)
    words = []                                              #List of single words in actual line
    for space in range(0, len(spaces)+1):
        if space == 0:
            word = line[:spaces[space]]
            words.append(word)
        elif space >=1 and space < len(spaces):
            word = line[spaces[space-1]:spaces[space]]
            word = word.strip()
            words.append(word)
        else:
            word = line[spaces[-1]:]
            word = word.strip()
            words.append(word)

    new_set = set(words)                                    #new set without duplicate elements

    if len(words) == len(new_set):                          #if size of element is equal then they haven't duplicate elements
        valid += 1

print(valid)
