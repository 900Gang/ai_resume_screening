import spacy
from spacy.matcher import PhraseMatcher

nlp = spacy.load("en_core_web_sm")

text =  """
I have experience with Python, Django, GitHub,
Machine Learning and Data Science.
"""

doc = nlp(text)

skills = [
    "python",
    "django",
    "github",
    "machine learning",
    "data science",
    "git",
    "sql"
]

matcher = PhraseMatcher(nlp.vocab)


patterns = [nlp.make_doc(skill) for skill in skills]

matcher.add("SKILL", patterns)

matches = matcher(doc)

for match_id, start, end in matches:
    span = doc[start:end]
    print(span.text)