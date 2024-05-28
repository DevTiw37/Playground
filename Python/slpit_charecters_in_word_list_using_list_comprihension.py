def splitWords2Char(sentence):
    sentence = sentence.split()
    sentence = [char for word in sentence for char in word]
    return sentence

sentence = input("Enter a sentence: ")
print(splitWords2Char(sentence))