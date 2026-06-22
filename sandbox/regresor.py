import random
import time
from collections import defaultdict

corpus = """
llm adalah model bahasa .
model ini bekerja secara autoregressive .
autoregressive berarti memprediksi token berikutnya .
token berikutnya bergantung pada token sebelumnya .
model bahasa ini sangat besar .
llm memprediksi kata demi kata .
setiap kata adalah token baru .
model ini belajar dari data .
"""

tokens = corpus.lower().split()
model = defaultdict(list)

for current_word, next_word in zip(tokens, tokens[1:]):
    model[current_word].append(next_word)

prompt = "berarti"
max_length = 15

generated_text = [prompt]
current_word = prompt

print(f"Prompt: {prompt}")
print(f"Generated: {current_word}", end=" ", flush=True)

for _ in range(max_length - 1):
    time.sleep(0.7)

    if current_word not in model:
        break

    possible_next_words = model[current_word]
    next_word = random.choice(possible_next_words)
    generated_text.append(next_word)
    print(f"{next_word}", end=" ", flush=True)
    current_word = next_word

    if current_word == ".":
        break
