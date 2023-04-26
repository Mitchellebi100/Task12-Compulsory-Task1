import spacy    #  code for importing spacy

nlp = spacy.load("en_core_web_md")  #code to return a Language object containing all components and data needed to process text.
print("\n\tSIMILARITY WITH SPACY\n")
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp ("banana")
print(word1.similarity(word2))  # code to print out the similarity with the word1 and word2
print(word3.similarity(word2))  # code to print out the similarity with the word3 and word2
print(word3.similarity(word1))  # code to print out the similarity with the word3 and word1

print("\n\tWORKING WITH VECTORS\n")
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

print("\n\tWORKING WITH SENTENCES\n")
sentence_to_compare = "Why is my cat on the car"    # code to compare this sentance with other sentances 
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:  # code to compare sentancs step by step
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity) # code for the similarities that will be printed out 

print("\n\tNOTE\n")
print("● Cat and monkey seem similar. Both of them are animals.;\n● Cat and banana does not have any significant similarity. I think because the cat usually does not eat banana. So, the model does not explicitly seem to recognise transitive relationships in its calculation;\n● Monkey and banana does have significant similarity. I think because the monkey likes to eat banana.\n")
