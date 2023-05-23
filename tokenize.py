import nltk

text = "James rides a bicycle"
tokens = nltk.word_tokenize(text)
ps_tags = nltk.pos_tag(tokens)

print(pos_tags)
