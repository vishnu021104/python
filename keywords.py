import keyword

words=['break','local','vishnu','john','continue','lambda','global']

for i in range(len(words)):
    if keyword.iskeyword(words[i]):
        print(words[i],"is a keyword in a python")
    else:
        print(words[i],"is not a keyword in a python")    