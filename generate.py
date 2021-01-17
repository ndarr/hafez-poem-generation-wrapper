import random
import requests
import json


with open("wordlist.10000", "r") as f:
    lines = f.readlines()
    words = [word.strip() for word in lines if len(word) > 3]


poems = []
n = 1000
for i in range(n):
    topic = random.choice(words)
    response = requests.get("http://0.0.0.0:8080/api/poem_check?topic="+ topic +"&k=1&model=0&id=3457&nline=14&encourage_words=&disencourage_words=&enc_weight=5&cword=-5&reps=0&allit=0&wordlen=0&topical=1&mono=-5&sentiment=0&concrete=0&is_default=1&source=advance")

    poem = response.json()['poem']

    poem = poem.replace("<br//>", "\n")

    stanzas = poem.split("\n\n")


    poem = "\n\n".join(stanzas[:2])
    poem = poem.replace("\n\n", "\n[NEWLINE]\n")
    poems.append(poem)
    print('Progress: %d/%d' % (i, n), end='\r')
    
with open("hafez_poems.txt", "w+") as f:
    output = "\n\n".join(poems)
    f.write(output)





