import spacy
from rich import print

# The spacy en_core_web_md model with the extracts from the T38 PDF
nlp = spacy.load("en_core_web_md")

tokens = nlp('cat apple monkey banana ')

for token1 in tokens:
    for token2 in tokens:
        print(f"""[blue]Token1 text: [bold]{token1.text}[/bold],
Token2 text:[bold]{token2.text}[/bold],
Similarity between [bold]{token1}[/bold] and [bold]{token2}[/bold]: {token1.similarity(token2)}[/blue]
""")


word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(f"[magenta]Similarity between [bold]{word1}[/bold] and [bold]{word2}[/bold]: {word1.similarity(word2)}[/magenta]")
print(f"[magenta]Similarity between [bold]{word3}[/bold] and [bold]{word2}[/bold]: {word3.similarity(word2)}[/magenta]")
print(f"[magenta]Similarity between [bold]{word3}[/bold] and [bold]{word1}[/bold]: {word3.similarity(word1)}[/magenta]")


sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
             "Hello, there is my car",
             "I\'ve lost my car in my car",
             "I\'d like my boat back",
             "I will name my dog Diana"]
print(f"\n[yellow]Initial sentence to compare against: [bold]{sentence_to_compare}[/bold][/yellow]")
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(f"[yellow]{sentence} - similarity to initial sentence: {similarity}[/yellow]")

# I found that the similarities interesting mainly from how accurate they seemed to be for word similarities.
# However, that accuracy wasn't as clear when it came to sentence similarities as in the last section.

# When running example.py with the en_core_web_sm model, for one it doesn't contain word vectors so similarities are
# based on tags, parser and NER.  This results in lower similarity scores for all comparisons. Word
# vector data allows for better accuracy by providing nuanced semantic meanings for words and sentences.
