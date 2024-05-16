# This program analyzes the number of characters present in the given text.

import pandas as pd

text = input("Enter your text: ").upper()
word_count = {}

for c in text:
    if c == " ":
        c=" Space"
    if c in word_count:
        word_count[c] += 1
    else:
        word_count[c] = 1
        


character = list(word_count.keys())
count = list(word_count.values())

data = pd.DataFrame({
    "Character":character,
    "Frequency":count
})

data.to_csv("result.csv",index=False)
print("check result.csv file")