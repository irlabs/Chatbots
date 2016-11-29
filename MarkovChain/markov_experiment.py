#!/usr/bin/env python

import markovify

with open("mobydick.txt") as f:
    text = f.read()
    
text_model = markovify.Text(text)

for i in range(5):
    print(text_model.make_sentence())
    
