import spacy

from  skill_extractor import extract_skills

nlp = spacy.load("en_core_web_sm")

text = "I have experience with Python, Django, GitHub,Machine Learning and Data Science."

doc = nlp(text)

text = extract_skills(text)

tokens = {token.text.lower() for token in doc}

print(tokens)

print("python:", "python" in tokens)
print("git:", "git" in tokens)
print("github:", "github" in tokens)
print("sql:", "sql" in tokens)
print("sqlalchemy:", "sqlalchemy" in tokens)