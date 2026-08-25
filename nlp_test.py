import spacy

nlp = spacy.load("en_core_web_sm")

text = """
Worked at Microsoft from 2024 to 2026.
I developed Python applications using Django.
"""

doc = nlp(text)

for entity in doc.ents:
    print("Text:", entity.text)
    print("Label:", entity.label_)
    print("Start:", entity.start)
    print("End:", entity.end)
    print()